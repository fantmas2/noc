# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------
# @workflow decorator
# ----------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import logging
# NOC modules
from noc.models import is_document

logger = logging.getLogger(__name__)


def fire_event(self, event):
    """
    Perform transition using event name
    :param event: event name
    :return:
    """
    self.state.fire_event(event, self)


def fire_transition(self, transition):
    """
    Perform transition
    :param transition: Transition instance
    :return:
    """
    self.state.fire_transition(transition, self)


def document_set_state(self, state):
    """
    Set state

    * Set field
    * Perform database update
    * Invalidate caches
    * Call State on_enter_handlers
    :param self:
    :param object:
    :return:
    """
    # Set field
    self.state = state
    # Update database directly
    # to avoid full save
    self._get_collection().update_one({
        "_id": self.id
    }, {
        "$set": {
            "state": state.id
        }
    })
    # Invalidate caches
    ic_handler = getattr(self, "invalidate_caches", None)
    if ic_handler:
        ic_handler()
    # Call state on_enter_handlers
    self.state.on_enter_state(self)


def model_set_state(self, state):
    """
    Set state

    * Set field
    * Perform database update
    * Invalidate caches
    * Call State on_enter_handlers
    :param self:
    :param object:
    :return:
    """
    # Set field
    self.state = state
    # Update database directly
    # to avoid full save
    self.objects.filter(id=self.id).update(state=str(state.id))
    # Invalidate caches
    ic_handler = getattr(self, "invalidate_caches", None)
    if ic_handler:
        ic_handler()
    # Call state on_enter_handlers
    self.state.on_enter_state(self)


def _on_document_post_save(sender, document, *args, **kwargs):
    if document.state is None:
        # No state, set default one
        # Get workflow
        profile = getattr(document, getattr(document, "PROFILE_LINK", "profile"))
        if not profile:
            logger.debug("[%s] Cannot set default state: No profile", document)
            return
        new_state = profile.workflow.get_default_state()
        if not new_state:
            logger.debug(
                "[%s] Cannot set default state: No default state for workflow %s",
                document, profile.workflow.name)
            return
        logger.debug("[%s] Set initial state to '%s'",
                     document, new_state.name)
        document.set_state(new_state)


def _on_model_post_save(sender, instance, *args, **kwargs):
    if instance.state is None:
        # No state, set default one
        # Get workflow
        profile = getattr(instance, getattr(instance, "PROFILE_LINK", "profile"))
        if not profile:
            logger.debug("[%s] Cannot set default state: No profile", instance)
            return
        new_state = profile.workflow.get_default_state()
        if not new_state:
            logger.debug(
                "[%s] Cannot set default state: No default state for workflow %s",
                instance, profile.workflow.name)
            return
        logger.debug("[%s] Set initial state to '%s'",
                     instance, new_state.name)
        instance.set_state(new_state)


def workflow(cls):
    """
    @workflow decorator denotes models which have .state
    field referring to WF State.

    Methods contributed to class:
    * set_state - change .state field with calling State.on_state_enter
    * fire_event - Perform transition using event name
    * fire_transition - Perform transition
    :return:
    """
    cls.fire_event = fire_event
    cls.fire_transition = fire_transition
    if is_document(cls):
        # MongoEngine model
        from mongoengine import signals as mongo_signals
        cls.set_state = document_set_state
        mongo_signals.post_save.connect(
            _on_document_post_save,
            sender=cls
        )
    else:
        # Django model
        from django.db.models import signals as django_signals
        cls.set_state = model_set_state
        django_signals.post_save.connect(
            _on_model_post_save,
            sender=cls
        )
    cls.fire_transition = fire_transition
    cls.fire_event = fire_event
    return cls
