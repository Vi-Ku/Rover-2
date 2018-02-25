# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_DriveTrain', [dirname(__file__)])
        except ImportError:
            import _DriveTrain
            return _DriveTrain
        if fp is not None:
            try:
                _mod = imp.load_module('_DriveTrain', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _DriveTrain = swig_import_helper()
    del swig_import_helper
else:
    import _DriveTrain
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_DriveTrain.RELATIVE_swigconstant(_DriveTrain)
RELATIVE = _DriveTrain.RELATIVE

_DriveTrain.ABSOLUTE_swigconstant(_DriveTrain)
ABSOLUTE = _DriveTrain.ABSOLUTE

_DriveTrain.PROFILE_POSITION_MODE_swigconstant(_DriveTrain)
PROFILE_POSITION_MODE = _DriveTrain.PROFILE_POSITION_MODE

_DriveTrain.PROFILE_VELOCITY_MODE_swigconstant(_DriveTrain)
PROFILE_VELOCITY_MODE = _DriveTrain.PROFILE_VELOCITY_MODE

_DriveTrain.POSITION_MODE_swigconstant(_DriveTrain)
POSITION_MODE = _DriveTrain.POSITION_MODE

_DriveTrain.VELOCITY_MODE_swigconstant(_DriveTrain)
VELOCITY_MODE = _DriveTrain.VELOCITY_MODE
class EposDriveTrain(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EposDriveTrain, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EposDriveTrain, name)
    __repr__ = _swig_repr
    __swig_getmethods__["MODVALUE"] = _DriveTrain.EposDriveTrain_MODVALUE_get
    if _newclass:
        MODVALUE = _swig_property(_DriveTrain.EposDriveTrain_MODVALUE_get)

    def __init__(self):
        this = _DriveTrain.new_EposDriveTrain()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_getmethods__["pi"] = _DriveTrain.EposDriveTrain_pi_get
    if _newclass:
        pi = _swig_property(_DriveTrain.EposDriveTrain_pi_get)
    __swig_getmethods__["START_OFFSET_ANGLE"] = _DriveTrain.EposDriveTrain_START_OFFSET_ANGLE_get
    if _newclass:
        START_OFFSET_ANGLE = _swig_property(_DriveTrain.EposDriveTrain_START_OFFSET_ANGLE_get)
    __swig_setmethods__["state"] = _DriveTrain.EposDriveTrain_state_set
    __swig_getmethods__["state"] = _DriveTrain.EposDriveTrain_state_get
    if _newclass:
        state = _swig_property(_DriveTrain.EposDriveTrain_state_get, _DriveTrain.EposDriveTrain_state_set)
    __swig_setmethods__["legStates"] = _DriveTrain.EposDriveTrain_legStates_set
    __swig_getmethods__["legStates"] = _DriveTrain.EposDriveTrain_legStates_get
    if _newclass:
        legStates = _swig_property(_DriveTrain.EposDriveTrain_legStates_get, _DriveTrain.EposDriveTrain_legStates_set)
    __swig_setmethods__["legAngles"] = _DriveTrain.EposDriveTrain_legAngles_set
    __swig_getmethods__["legAngles"] = _DriveTrain.EposDriveTrain_legAngles_get
    if _newclass:
        legAngles = _swig_property(_DriveTrain.EposDriveTrain_legAngles_get, _DriveTrain.EposDriveTrain_legAngles_set)
    __swig_setmethods__["targetPos"] = _DriveTrain.EposDriveTrain_targetPos_set
    __swig_getmethods__["targetPos"] = _DriveTrain.EposDriveTrain_targetPos_get
    if _newclass:
        targetPos = _swig_property(_DriveTrain.EposDriveTrain_targetPos_get, _DriveTrain.EposDriveTrain_targetPos_set)
    __swig_getmethods__["legAirSpeed"] = _DriveTrain.EposDriveTrain_legAirSpeed_get
    if _newclass:
        legAirSpeed = _swig_property(_DriveTrain.EposDriveTrain_legAirSpeed_get)
    __swig_getmethods__["landingAngle"] = _DriveTrain.EposDriveTrain_landingAngle_get
    if _newclass:
        landingAngle = _swig_property(_DriveTrain.EposDriveTrain_landingAngle_get)
    __swig_getmethods__["legGroundSpeed"] = _DriveTrain.EposDriveTrain_legGroundSpeed_get
    if _newclass:
        legGroundSpeed = _swig_property(_DriveTrain.EposDriveTrain_legGroundSpeed_get)
    __swig_getmethods__["FRONTLEFT"] = _DriveTrain.EposDriveTrain_FRONTLEFT_get
    if _newclass:
        FRONTLEFT = _swig_property(_DriveTrain.EposDriveTrain_FRONTLEFT_get)
    __swig_getmethods__["MIDDLELEFT"] = _DriveTrain.EposDriveTrain_MIDDLELEFT_get
    if _newclass:
        MIDDLELEFT = _swig_property(_DriveTrain.EposDriveTrain_MIDDLELEFT_get)
    __swig_getmethods__["BACKLEFT"] = _DriveTrain.EposDriveTrain_BACKLEFT_get
    if _newclass:
        BACKLEFT = _swig_property(_DriveTrain.EposDriveTrain_BACKLEFT_get)
    __swig_getmethods__["FRONTRIGHT"] = _DriveTrain.EposDriveTrain_FRONTRIGHT_get
    if _newclass:
        FRONTRIGHT = _swig_property(_DriveTrain.EposDriveTrain_FRONTRIGHT_get)
    __swig_getmethods__["MIDDLERIGHT"] = _DriveTrain.EposDriveTrain_MIDDLERIGHT_get
    if _newclass:
        MIDDLERIGHT = _swig_property(_DriveTrain.EposDriveTrain_MIDDLERIGHT_get)
    __swig_getmethods__["BACKRIGHT"] = _DriveTrain.EposDriveTrain_BACKRIGHT_get
    if _newclass:
        BACKRIGHT = _swig_property(_DriveTrain.EposDriveTrain_BACKRIGHT_get)
    __swig_getmethods__["accel"] = _DriveTrain.EposDriveTrain_accel_get
    if _newclass:
        accel = _swig_property(_DriveTrain.EposDriveTrain_accel_get)
    __swig_getmethods__["deccel"] = _DriveTrain.EposDriveTrain_deccel_get
    if _newclass:
        deccel = _swig_property(_DriveTrain.EposDriveTrain_deccel_get)
    __swig_destroy__ = _DriveTrain.delete_EposDriveTrain
    __del__ = lambda self: None

    def init(self):
        return _DriveTrain.EposDriveTrain_init(self)

    def setMode(self, arg2, arg3):
        return _DriveTrain.EposDriveTrain_setMode(self, arg2, arg3)

    def setVelocity(self, arg2, arg3):
        return _DriveTrain.EposDriveTrain_setVelocity(self, arg2, arg3)

    def setVelocityProfile(self, arg2, arg3, arg4):
        return _DriveTrain.EposDriveTrain_setVelocityProfile(self, arg2, arg3, arg4)

    def setPosition(self, arg2, arg3, arg4):
        return _DriveTrain.EposDriveTrain_setPosition(self, arg2, arg3, arg4)

    def setPositionProfile(self, arg2, arg3, arg4, arg5):
        return _DriveTrain.EposDriveTrain_setPositionProfile(self, arg2, arg3, arg4, arg5)

    def halt(self, arg2):
        return _DriveTrain.EposDriveTrain_halt(self, arg2)

    def stopAllMotors(self):
        return _DriveTrain.EposDriveTrain_stopAllMotors(self)

    def enableNode(self, arg2):
        return _DriveTrain.EposDriveTrain_enableNode(self, arg2)

    def disableNode(self, arg2):
        return _DriveTrain.EposDriveTrain_disableNode(self, arg2)

    def clearFault(self, arg2):
        return _DriveTrain.EposDriveTrain_clearFault(self, arg2)

    def enableAll(self):
        return _DriveTrain.EposDriveTrain_enableAll(self)

    def disableAll(self):
        return _DriveTrain.EposDriveTrain_disableAll(self)

    def clearAllFaults(self):
        return _DriveTrain.EposDriveTrain_clearAllFaults(self)

    def getPosition(self, arg2):
        return _DriveTrain.EposDriveTrain_getPosition(self, arg2)

    def getVelocity(self, arg2):
        return _DriveTrain.EposDriveTrain_getVelocity(self, arg2)

    def isAtTarget(self, arg2):
        return _DriveTrain.EposDriveTrain_isAtTarget(self, arg2)

    def getCurrent(self, arg2):
        return _DriveTrain.EposDriveTrain_getCurrent(self, arg2)

    def getGoalPos(self, arg2, arg3, arg4, arg5):
        return _DriveTrain.EposDriveTrain_getGoalPos(self, arg2, arg3, arg4, arg5)

    def moveLegs(self, arg2, arg3, arg4):
        return _DriveTrain.EposDriveTrain_moveLegs(self, arg2, arg3, arg4)

    def allAreAtTargets(self):
        return _DriveTrain.EposDriveTrain_allAreAtTargets(self)

    def isCloseEnough(self, arg2, arg3):
        return _DriveTrain.EposDriveTrain_isCloseEnough(self, arg2, arg3)

    def areAllCloseEnough(self, arg2):
        return _DriveTrain.EposDriveTrain_areAllCloseEnough(self, arg2)
EposDriveTrain_swigregister = _DriveTrain.EposDriveTrain_swigregister
EposDriveTrain_swigregister(EposDriveTrain)

# This file is compatible with both classic and new-style classes.


