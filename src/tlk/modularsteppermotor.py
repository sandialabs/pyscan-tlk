from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_float,
    c_int,
    c_int32,
    c_long,
    c_short,
    c_uint,
    cdll,
    pointer)
from .definitions.enumerations import (
    MOT_JogModes,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchSWModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_JoystickParameters,
    MOT_LimitSwitchParameters,
    MOT_PowerParameters,
    MOT_VelocityParameters)
from .definitions.kinesisexception import KinesisException

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Modular.DLL")

SBC_CanHome = lib.SBC_CanHome
SBC_CanHome.restype = c_bool
SBC_CanHome.argtypes = []


def can_home(serial_number):
    '''
    Can the device perform a Home.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_CanHome(serial_number)

    return output


SBC_CanMoveWithoutHomingFirst = lib.SBC_CanMoveWithoutHomingFirst
SBC_CanMoveWithoutHomingFirst.restype = c_bool
SBC_CanMoveWithoutHomingFirst.argtypes = []


def can_move_without_homing_first(serial_number):
    '''
    Can this device be moved without Homing.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_CanMoveWithoutHomingFirst(serial_number)

    return output


SBC_DisableChannel = lib.SBC_DisableChannel
SBC_DisableChannel.restype = c_short
SBC_DisableChannel.argtypes = []


def disable_channel(serial_number):
    '''
    Disable the channel so that motor can be moved by hand.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_DisableChannel(serial_number)

    return output


SBC_EnableChannel = lib.SBC_EnableChannel
SBC_EnableChannel.restype = c_short
SBC_EnableChannel.argtypes = []


def enable_channel(serial_number):
    '''
    Enable channel for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_EnableChannel(serial_number)

    return output


SBC_EnableLastMsgTimer = lib.SBC_EnableLastMsgTimer
SBC_EnableLastMsgTimer.restype = c_void_p
SBC_EnableLastMsgTimer.argtypes = []


def enable_last_msg_timer(serial_number):
    '''
    Enables the last message monitoring timer.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        enable: c_bool
        lastMsgTimeout: c_int32

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SBC_EnableLastMsgTimer(serial_number)

    return output


SBC_GetBacklash = lib.SBC_GetBacklash
SBC_GetBacklash.restype = c_long
SBC_GetBacklash.argtypes = []


def get_backlash(serial_number):
    '''
    Get the backlash distance setting (used to control hysteresis).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetBacklash(serial_number)

    return output


SBC_GetBowIndex = lib.SBC_GetBowIndex
SBC_GetBowIndex.restype = c_short
SBC_GetBowIndex.argtypes = []


def get_bow_index(serial_number):
    '''
    Gets the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetBowIndex(serial_number)

    return output


SBC_GetCalibrationFile = lib.SBC_GetCalibrationFile
SBC_GetCalibrationFile.restype = c_bool
SBC_GetCalibrationFile.argtypes = []


def get_calibration_file(serial_number):
    '''
    Get calibration file for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        filename: POINTER(c_char)
        sizeOfBuffer: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    filename = POINTER(c_char)()
    sizeOfBuffer = c_short()

    output = SBC_GetCalibrationFile(serial_number)

    return output


SBC_GetDeviceUnitFromRealValue = lib.SBC_GetDeviceUnitFromRealValue
SBC_GetDeviceUnitFromRealValue.restype = c_short
SBC_GetDeviceUnitFromRealValue.argtypes = []


def get_device_unit_from_real_value(serial_number):
    '''
    Converts a device unit to a real world unit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        real_unit: c_double
        device_unit: c_int
        unitType: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = SBC_GetDeviceUnitFromRealValue(serial_number)

    return output


SBC_GetDigitalOutputs = lib.SBC_GetDigitalOutputs
SBC_GetDigitalOutputs.restype = c_byte
SBC_GetDigitalOutputs.argtypes = []


def get_digital_outputs(serial_number):
    '''
    Gets the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetDigitalOutputs(serial_number)

    return output


SBC_GetEncoderCounter = lib.SBC_GetEncoderCounter
SBC_GetEncoderCounter.restype = c_long
SBC_GetEncoderCounter.argtypes = []


def get_encoder_counter(serial_number):
    '''
    Get the Encoder Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetEncoderCounter(serial_number)

    return output


SBC_GetHomingParamsBlock = lib.SBC_GetHomingParamsBlock
SBC_GetHomingParamsBlock.restype = c_short
SBC_GetHomingParamsBlock.argtypes = []


def get_homing_params_block(serial_number):
    '''
    Get the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        homingParams: MOT_HomingParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = SBC_GetHomingParamsBlock(serial_number)

    return output


SBC_GetHomingVelocity = lib.SBC_GetHomingVelocity
SBC_GetHomingVelocity.restype = c_uint
SBC_GetHomingVelocity.argtypes = []


def get_homing_velocity(serial_number):
    '''
    Gets the homing velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetHomingVelocity(serial_number)

    return output


SBC_GetInputVoltage = lib.SBC_GetInputVoltage
SBC_GetInputVoltage.restype = c_long
SBC_GetInputVoltage.argtypes = []


def get_input_voltage(serial_number):
    '''
    Gets the analogue input voltage reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetInputVoltage(serial_number)

    return output


SBC_GetJogMode = lib.SBC_GetJogMode
SBC_GetJogMode.restype = c_short
SBC_GetJogMode.argtypes = []


def get_jog_mode(serial_number):
    '''
    Gets the jog mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        mode: MOT_JogModes
        stopMode: MOT_StopModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SBC_GetJogMode(serial_number)

    return output


SBC_GetJogParamsBlock = lib.SBC_GetJogParamsBlock
SBC_GetJogParamsBlock.restype = c_short
SBC_GetJogParamsBlock.argtypes = []


def get_jog_params_block(serial_number):
    '''
    Get the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        jogParams: MOT_JogParameters
        jogParameters: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    jogParams = MOT_JogParameters()
    jogParameters = MOT_JogParameters()

    output = SBC_GetJogParamsBlock(serial_number)

    return output


SBC_GetJogStepSize = lib.SBC_GetJogStepSize
SBC_GetJogStepSize.restype = c_uint
SBC_GetJogStepSize.argtypes = []


def get_jog_step_size(serial_number):
    '''
    Gets the distance to move when jogging.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetJogStepSize(serial_number)

    return output


SBC_GetJogVelParams = lib.SBC_GetJogVelParams
SBC_GetJogVelParams.restype = c_short
SBC_GetJogVelParams.argtypes = []


def get_jog_vel_params(serial_number):
    '''
    Gets the jog velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_GetJogVelParams(serial_number)

    return output


SBC_GetJoystickParams = lib.SBC_GetJoystickParams
SBC_GetJoystickParams.restype = c_short
SBC_GetJoystickParams.argtypes = []


def get_joystick_params(serial_number):
    '''
    Gets the joystick parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        joystickParams: MOT_JoystickParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    joystickParams = MOT_JoystickParameters()

    output = SBC_GetJoystickParams(serial_number)

    return output


SBC_GetLimitSwitchParams = lib.SBC_GetLimitSwitchParams
SBC_GetLimitSwitchParams.restype = c_short
SBC_GetLimitSwitchParams.argtypes = []


def get_limit_switch_params(serial_number):
    '''
    Gets the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        clockwiseHardwareLimit: MOT_LimitSwitchModes
        anticlockwiseHardwareLimit: MOT_LimitSwitchModes
        clockwisePosition: c_uint
        anticlockwisePosition: c_uint
        softLimitMode: MOT_LimitSwitchSWModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = SBC_GetLimitSwitchParams(serial_number)

    return output


SBC_GetLimitSwitchParamsBlock = lib.SBC_GetLimitSwitchParamsBlock
SBC_GetLimitSwitchParamsBlock.restype = c_short
SBC_GetLimitSwitchParamsBlock.argtypes = []


def get_limit_switch_params_block(serial_number):
    '''
    Get the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        limitSwitchParams: MOT_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SBC_GetLimitSwitchParamsBlock(serial_number)

    return output


SBC_GetMotorParams = lib.SBC_GetMotorParams
SBC_GetMotorParams.restype = c_short
SBC_GetMotorParams.argtypes = []


def get_motor_params(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stepsPerRev: c_long
        gearBoxRatio: c_long
        pitch: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SBC_GetMotorParams(serial_number)

    return output


SBC_GetMotorParamsExt = lib.SBC_GetMotorParamsExt
SBC_GetMotorParamsExt.restype = c_short
SBC_GetMotorParamsExt.argtypes = []


def get_motor_params_ext(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stepsPerRev: c_double
        gearBoxRatio: c_double
        pitch: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SBC_GetMotorParamsExt(serial_number)

    return output


SBC_GetMotorTravelLimits = lib.SBC_GetMotorTravelLimits
SBC_GetMotorTravelLimits.restype = c_short
SBC_GetMotorTravelLimits.argtypes = []


def get_motor_travel_limits(serial_number):
    '''
    Gets the absolute minimum and maximum travel range constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        minPosition: c_double
        maxPosition: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = SBC_GetMotorTravelLimits(serial_number)

    return output


SBC_GetMotorTravelMode = lib.SBC_GetMotorTravelMode
SBC_GetMotorTravelMode.restype = MOT_TravelModes
SBC_GetMotorTravelMode.argtypes = []


def get_motor_travel_mode(serial_number):
    '''
    Get the motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        MOT_TravelModes
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetMotorTravelMode(serial_number)

    return output


SBC_GetMotorVelocityLimits = lib.SBC_GetMotorVelocityLimits
SBC_GetMotorVelocityLimits.restype = c_short
SBC_GetMotorVelocityLimits.argtypes = []


def get_motor_velocity_limits(serial_number):
    '''
    Gets the absolute maximum velocity and acceleration constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        maxVelocity: c_double
        maxAcceleration: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SBC_GetMotorVelocityLimits(serial_number)

    return output


SBC_GetMoveAbsolutePosition = lib.SBC_GetMoveAbsolutePosition
SBC_GetMoveAbsolutePosition.restype = c_int
SBC_GetMoveAbsolutePosition.argtypes = []


def get_move_absolute_position(serial_number):
    '''
    Gets the move absolute position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetMoveAbsolutePosition(serial_number)

    return output


SBC_GetMoveRelativeDistance = lib.SBC_GetMoveRelativeDistance
SBC_GetMoveRelativeDistance.restype = c_int
SBC_GetMoveRelativeDistance.argtypes = []


def get_move_relative_distance(serial_number):
    '''
    Gets the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetMoveRelativeDistance(serial_number)

    return output


SBC_GetNumberPositions = lib.SBC_GetNumberPositions
SBC_GetNumberPositions.restype = c_int
SBC_GetNumberPositions.argtypes = []


def get_number_positions(serial_number):
    '''
    Get number of positions.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetNumberPositions(serial_number)

    return output


SBC_GetPosition = lib.SBC_GetPosition
SBC_GetPosition.restype = c_int
SBC_GetPosition.argtypes = []


def get_position(serial_number):
    '''
    Get the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetPosition(serial_number)

    return output


SBC_GetPositionCounter = lib.SBC_GetPositionCounter
SBC_GetPositionCounter.restype = c_long
SBC_GetPositionCounter.argtypes = []


def get_position_counter(serial_number):
    '''
    Get the Position Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetPositionCounter(serial_number)

    return output


SBC_GetPowerParams = lib.SBC_GetPowerParams
SBC_GetPowerParams.restype = c_short
SBC_GetPowerParams.argtypes = []


def get_power_params(serial_number):
    '''
    Sets the power parameters for the stepper motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        powerParams: MOT_PowerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    powerParams = MOT_PowerParameters()

    output = SBC_GetPowerParams(serial_number)

    return output


SBC_GetRealValueFromDeviceUnit = lib.SBC_GetRealValueFromDeviceUnit
SBC_GetRealValueFromDeviceUnit.restype = c_short
SBC_GetRealValueFromDeviceUnit.argtypes = []


def get_real_value_from_device_unit(serial_number):
    '''
    Converts a device unit to a real world unit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        device_unit: c_int
        real_unit: c_double
        unitType: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = SBC_GetRealValueFromDeviceUnit(serial_number)

    return output


SBC_GetSoftLimitMode = lib.SBC_GetSoftLimitMode
SBC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SBC_GetSoftLimitMode.argtypes = []


def get_soft_limit_mode(serial_number):
    '''
    Gets the software limits mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        MOT_LimitsSoftwareApproachPolicy
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetSoftLimitMode(serial_number)

    return output


SBC_GetStageAxisMaxPos = lib.SBC_GetStageAxisMaxPos
SBC_GetStageAxisMaxPos.restype = c_int
SBC_GetStageAxisMaxPos.argtypes = []


def get_stage_axis_max_pos(serial_number):
    '''
    Gets the Stepper Motor maximum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetStageAxisMaxPos(serial_number)

    return output


SBC_GetStageAxisMinPos = lib.SBC_GetStageAxisMinPos
SBC_GetStageAxisMinPos.restype = c_int
SBC_GetStageAxisMinPos.argtypes = []


def get_stage_axis_min_pos(serial_number):
    '''
    Gets the Stepper Motor minimum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetStageAxisMinPos(serial_number)

    return output


SBC_GetStatusBits = lib.SBC_GetStatusBits
SBC_GetStatusBits.restype = c_ulong
SBC_GetStatusBits.argtypes = []


def get_status_bits(serial_number):
    '''
    Get the current status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetStatusBits(serial_number)

    return output


SBC_GetTriggerSwitches = lib.SBC_GetTriggerSwitches
SBC_GetTriggerSwitches.restype = c_byte
SBC_GetTriggerSwitches.argtypes = []


def get_trigger_switches(serial_number):
    '''
    Gets the trigger switch parameter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_GetTriggerSwitches(serial_number)

    return output


SBC_GetVelParams = lib.SBC_GetVelParams
SBC_GetVelParams.restype = c_short
SBC_GetVelParams.argtypes = []


def get_vel_params(serial_number):
    '''
    Gets the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_GetVelParams(serial_number)

    return output


SBC_GetVelParamsBlock = lib.SBC_GetVelParamsBlock
SBC_GetVelParamsBlock.restype = c_short
SBC_GetVelParamsBlock.argtypes = []


def get_vel_params_block(serial_number):
    '''
    Get the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocityParams: MOT_VelocityParameters
        velocityParameters: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()
    velocityParameters = MOT_VelocityParameters()

    output = SBC_GetVelParamsBlock(serial_number)

    return output


SBC_HasLastMsgTimerOverrun = lib.SBC_HasLastMsgTimerOverrun
SBC_HasLastMsgTimerOverrun.restype = c_bool
SBC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by SBC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_HasLastMsgTimerOverrun(serial_number)

    return output


SBC_Home = lib.SBC_Home
SBC_Home.restype = c_short
SBC_Home.argtypes = []


def home(serial_number):
    '''
    Home the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_Home(serial_number)

    return output


SBC_IsCalibrationActive = lib.SBC_IsCalibrationActive
SBC_IsCalibrationActive.restype = c_bool
SBC_IsCalibrationActive.argtypes = []


def is_calibration_active(serial_number):
    '''
    Is a calibration file active for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_IsCalibrationActive(serial_number)

    return output


SBC_MoveAbsolute = lib.SBC_MoveAbsolute
SBC_MoveAbsolute.restype = c_short
SBC_MoveAbsolute.argtypes = []


def move_absolute(serial_number):
    '''
    Moves the device to the position defined in the SetMoveAbsolute command.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_MoveAbsolute(serial_number)

    return output


SBC_MoveAtVelocity = lib.SBC_MoveAtVelocity
SBC_MoveAtVelocity.restype = c_short
SBC_MoveAtVelocity.argtypes = []


def move_at_velocity(serial_number):
    '''
    Start moving at the current velocity in the specified direction.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        direction: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    direction = MOT_TravelDirection()

    output = SBC_MoveAtVelocity(serial_number)

    return output


SBC_MoveJog = lib.SBC_MoveJog
SBC_MoveJog.restype = c_short
SBC_MoveJog.argtypes = []


def move_jog(serial_number):
    '''
    Perform a jog.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        jogDirection: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    jogDirection = MOT_TravelDirection()

    output = SBC_MoveJog(serial_number)

    return output


SBC_MoveRelative = lib.SBC_MoveRelative
SBC_MoveRelative.restype = c_short
SBC_MoveRelative.argtypes = []


def move_relative(serial_number):
    '''
    Move the motor by a relative amount.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        displacement: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    displacement = c_int()

    output = SBC_MoveRelative(serial_number)

    return output


SBC_MoveRelativeDistance = lib.SBC_MoveRelativeDistance
SBC_MoveRelativeDistance.restype = c_short
SBC_MoveRelativeDistance.argtypes = []


def move_relative_distance(serial_number):
    '''
    Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_MoveRelativeDistance(serial_number)

    return output


SBC_MoveToPosition = lib.SBC_MoveToPosition
SBC_MoveToPosition.restype = c_short
SBC_MoveToPosition.argtypes = []


def move_to_position(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        index: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    index = c_int()

    output = SBC_MoveToPosition(serial_number)

    return output


SBC_NeedsHoming = lib.SBC_NeedsHoming
SBC_NeedsHoming.restype = c_bool
SBC_NeedsHoming.argtypes = []


def needs_homing(serial_number):
    '''
    Does the device need to be Homed before a move can be performed.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_NeedsHoming(serial_number)

    return output


SBC_PollingDuration = lib.SBC_PollingDuration
SBC_PollingDuration.restype = c_long
SBC_PollingDuration.argtypes = []


def polling_duration(serial_number):
    '''
    Gets the polling loop duration.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_PollingDuration(serial_number)

    return output


SBC_RequestDigitalOutputs = lib.SBC_RequestDigitalOutputs
SBC_RequestDigitalOutputs.restype = c_short
SBC_RequestDigitalOutputs.argtypes = []


def request_digital_outputs(serial_number):
    '''
    Requests the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_RequestDigitalOutputs(serial_number)

    return output


SBC_RequestInputVoltage = lib.SBC_RequestInputVoltage
SBC_RequestInputVoltage.restype = c_short
SBC_RequestInputVoltage.argtypes = []


def request_input_voltage(serial_number):
    '''
    Requests the analogue input voltage reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_RequestInputVoltage(serial_number)

    return output


SBC_RequestPosition = lib.SBC_RequestPosition
SBC_RequestPosition.restype = c_short
SBC_RequestPosition.argtypes = []


def request_position(serial_number):
    '''
    Requests the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_RequestPosition(serial_number)

    return output


SBC_RequestSettings = lib.SBC_RequestSettings
SBC_RequestSettings.restype = c_short
SBC_RequestSettings.argtypes = []


def request_settings(serial_number):
    '''
    Requests that all settings are download from device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_RequestSettings(serial_number)

    return output


SBC_RequestStatusBits = lib.SBC_RequestStatusBits
SBC_RequestStatusBits.restype = c_short
SBC_RequestStatusBits.argtypes = []


def request_status_bits(serial_number):
    '''
    Request the status bits which identify the current motor state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_RequestStatusBits(serial_number)

    return output


SBC_ResetRotationModes = lib.SBC_ResetRotationModes
SBC_ResetRotationModes.restype = c_short
SBC_ResetRotationModes.argtypes = []


def reset_rotation_modes(serial_number):
    '''
    Reset the rotation modes for a rotational device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_ResetRotationModes(serial_number)

    return output


SBC_ResumeMoveMessages = lib.SBC_ResumeMoveMessages
SBC_ResumeMoveMessages.restype = c_short
SBC_ResumeMoveMessages.argtypes = []


def resume_move_messages(serial_number):
    '''
    Resume suspended move messages.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_ResumeMoveMessages(serial_number)

    return output


SBC_SetBacklash = lib.SBC_SetBacklash
SBC_SetBacklash.restype = c_short
SBC_SetBacklash.argtypes = []


def set_backlash(serial_number):
    '''
    Sets the backlash distance (used to control hysteresis).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        distance: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    distance = c_long()

    output = SBC_SetBacklash(serial_number)

    return output


SBC_SetBowIndex = lib.SBC_SetBowIndex
SBC_SetBowIndex.restype = c_short
SBC_SetBowIndex.argtypes = []


def set_bow_index(serial_number):
    '''
    Sets the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        bowIndex: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    bowIndex = c_short()

    output = SBC_SetBowIndex(serial_number)

    return output


SBC_SetCalibrationFile = lib.SBC_SetCalibrationFile
SBC_SetCalibrationFile.restype = c_void_p
SBC_SetCalibrationFile.argtypes = []


def set_calibration_file(serial_number):
    '''
    Set the calibration file for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        filename: POINTER(c_char)
        enabled: c_bool

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    filename = POINTER(c_char)()
    enabled = c_bool()

    output = SBC_SetCalibrationFile(serial_number)

    return output


SBC_SetDigitalOutputs = lib.SBC_SetDigitalOutputs
SBC_SetDigitalOutputs.restype = c_short
SBC_SetDigitalOutputs.argtypes = []


def set_digital_outputs(serial_number):
    '''
    Sets the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        outputsBits: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    outputsBits = c_byte()

    output = SBC_SetDigitalOutputs(serial_number)

    return output


SBC_SetDirection = lib.SBC_SetDirection
SBC_SetDirection.restype = c_short
SBC_SetDirection.argtypes = []


def set_direction(serial_number):
    '''
    Sets the motor direction sense.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        reverse: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    reverse = c_bool()

    output = SBC_SetDirection(serial_number)

    return output


SBC_SetEncoderCounter = lib.SBC_SetEncoderCounter
SBC_SetEncoderCounter.restype = c_short
SBC_SetEncoderCounter.argtypes = []


def set_encoder_counter(serial_number):
    '''
    Set the Encoder Counter values.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        count: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    count = c_long()

    output = SBC_SetEncoderCounter(serial_number)

    return output


SBC_SetHomingParamsBlock = lib.SBC_SetHomingParamsBlock
SBC_SetHomingParamsBlock.restype = c_short
SBC_SetHomingParamsBlock.argtypes = []


def set_homing_params_block(serial_number):
    '''
    Set the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        homingParams: MOT_HomingParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = SBC_SetHomingParamsBlock(serial_number)

    return output


SBC_SetHomingVelocity = lib.SBC_SetHomingVelocity
SBC_SetHomingVelocity.restype = c_short
SBC_SetHomingVelocity.argtypes = []


def set_homing_velocity(serial_number):
    '''
    Sets the homing velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocity: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocity = c_uint()

    output = SBC_SetHomingVelocity(serial_number)

    return output


SBC_SetJogMode = lib.SBC_SetJogMode
SBC_SetJogMode.restype = c_short
SBC_SetJogMode.argtypes = []


def set_jog_mode(serial_number):
    '''
    Sets the jog mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        mode: MOT_JogModes
        stopMode: MOT_StopModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SBC_SetJogMode(serial_number)

    return output


SBC_SetJogParamsBlock = lib.SBC_SetJogParamsBlock
SBC_SetJogParamsBlock.restype = c_short
SBC_SetJogParamsBlock.argtypes = []


def set_jog_params_block(serial_number):
    '''
    Set the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        jogParams: MOT_JogParameters
        jogParameters: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    jogParams = MOT_JogParameters()
    jogParameters = MOT_JogParameters()

    output = SBC_SetJogParamsBlock(serial_number)

    return output


SBC_SetJogStepSize = lib.SBC_SetJogStepSize
SBC_SetJogStepSize.restype = c_short
SBC_SetJogStepSize.argtypes = []


def set_jog_step_size(serial_number):
    '''
    Sets the distance to move on jogging.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stepSize: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stepSize = c_uint()

    output = SBC_SetJogStepSize(serial_number)

    return output


SBC_SetJogVelParams = lib.SBC_SetJogVelParams
SBC_SetJogVelParams.restype = c_short
SBC_SetJogVelParams.argtypes = []


def set_jog_vel_params(serial_number):
    '''
    Sets jog velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_SetJogVelParams(serial_number)

    return output


SBC_SetJoystickParams = lib.SBC_SetJoystickParams
SBC_SetJoystickParams.restype = c_short
SBC_SetJoystickParams.argtypes = []


def set_joystick_params(serial_number):
    '''
    Sets the joystick parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        joystickParams: MOT_JoystickParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    joystickParams = MOT_JoystickParameters()

    output = SBC_SetJoystickParams(serial_number)

    return output


SBC_SetLimitSwitchParams = lib.SBC_SetLimitSwitchParams
SBC_SetLimitSwitchParams.restype = c_short
SBC_SetLimitSwitchParams.argtypes = []


def set_limit_switch_params(serial_number):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        clockwiseHardwareLimit: MOT_LimitSwitchModes
        anticlockwiseHardwareLimit: MOT_LimitSwitchModes
        clockwisePosition: c_uint
        anticlockwisePosition: c_uint
        softLimitMode: MOT_LimitSwitchSWModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = SBC_SetLimitSwitchParams(serial_number)

    return output


SBC_SetLimitSwitchParamsBlock = lib.SBC_SetLimitSwitchParamsBlock
SBC_SetLimitSwitchParamsBlock.restype = c_short
SBC_SetLimitSwitchParamsBlock.argtypes = []


def set_limit_switch_params_block(serial_number):
    '''
    Set the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        limitSwitchParams: MOT_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SBC_SetLimitSwitchParamsBlock(serial_number)

    return output


SBC_SetLimitsSoftwareApproachPolicy = lib.SBC_SetLimitsSoftwareApproachPolicy
SBC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SBC_SetLimitsSoftwareApproachPolicy.argtypes = []


def set_limits_software_approach_policy(serial_number):
    '''
    Sets the software limits mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        limitsSoftwareApproachPolicy: MOT_LimitsSoftwareApproachPolicy

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = SBC_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


SBC_SetMotorParams = lib.SBC_SetMotorParams
SBC_SetMotorParams.restype = c_short
SBC_SetMotorParams.argtypes = []


def set_motor_params(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stepsPerRev: c_long
        gearBoxRatio: c_long
        pitch: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SBC_SetMotorParams(serial_number)

    return output


SBC_SetMotorParamsExt = lib.SBC_SetMotorParamsExt
SBC_SetMotorParamsExt.restype = c_short
SBC_SetMotorParamsExt.argtypes = []


def set_motor_params_ext(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stepsPerRev: c_double
        gearBoxRatio: c_double
        pitch: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SBC_SetMotorParamsExt(serial_number)

    return output


SBC_SetMotorTravelLimits = lib.SBC_SetMotorTravelLimits
SBC_SetMotorTravelLimits.restype = c_short
SBC_SetMotorTravelLimits.argtypes = []


def set_motor_travel_limits(serial_number):
    '''
    Sets the absolute minimum and maximum travel range constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        minPosition: c_double
        maxPosition: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = SBC_SetMotorTravelLimits(serial_number)

    return output


SBC_SetMotorTravelMode = lib.SBC_SetMotorTravelMode
SBC_SetMotorTravelMode.restype = c_short
SBC_SetMotorTravelMode.argtypes = []


def set_motor_travel_mode(serial_number):
    '''
    Set the motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        travelMode: MOT_TravelModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    travelMode = MOT_TravelModes()

    output = SBC_SetMotorTravelMode(serial_number)

    return output


SBC_SetMotorVelocityLimits = lib.SBC_SetMotorVelocityLimits
SBC_SetMotorVelocityLimits.restype = c_short
SBC_SetMotorVelocityLimits.argtypes = []


def set_motor_velocity_limits(serial_number):
    '''
    Sets the absolute maximum velocity and acceleration constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        maxVelocity: c_double
        maxAcceleration: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SBC_SetMotorVelocityLimits(serial_number)

    return output


SBC_SetMoveAbsolutePosition = lib.SBC_SetMoveAbsolutePosition
SBC_SetMoveAbsolutePosition.restype = c_short
SBC_SetMoveAbsolutePosition.argtypes = []


def set_move_absolute_position(serial_number):
    '''
    Sets the move absolute position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        position: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    position = c_int()

    output = SBC_SetMoveAbsolutePosition(serial_number)

    return output


SBC_SetMoveRelativeDistance = lib.SBC_SetMoveRelativeDistance
SBC_SetMoveRelativeDistance.restype = c_short
SBC_SetMoveRelativeDistance.argtypes = []


def set_move_relative_distance(serial_number):
    '''
    Sets the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        distance: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    distance = c_int()

    output = SBC_SetMoveRelativeDistance(serial_number)

    return output


SBC_SetPositionCounter = lib.SBC_SetPositionCounter
SBC_SetPositionCounter.restype = c_short
SBC_SetPositionCounter.argtypes = []


def set_position_counter(serial_number):
    '''
    Set the Position Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        count: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    count = c_long()

    output = SBC_SetPositionCounter(serial_number)

    return output


SBC_SetPowerParams = lib.SBC_SetPowerParams
SBC_SetPowerParams.restype = c_short
SBC_SetPowerParams.argtypes = []


def set_power_params(serial_number):
    '''
    Sets the power parameters for the stepper motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        powerParams: MOT_PowerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    powerParams = MOT_PowerParameters()

    output = SBC_SetPowerParams(serial_number)

    return output


SBC_SetRotationModes = lib.SBC_SetRotationModes
SBC_SetRotationModes.restype = c_short
SBC_SetRotationModes.argtypes = []


def set_rotation_modes(serial_number):
    '''
    Set the rotation modes for a rotational device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        mode: MOT_MovementModes
        direction: MOT_MovementDirections

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = SBC_SetRotationModes(serial_number)

    return output


SBC_SetStageAxisLimits = lib.SBC_SetStageAxisLimits
SBC_SetStageAxisLimits.restype = c_short
SBC_SetStageAxisLimits.argtypes = []


def set_stage_axis_limits(serial_number):
    '''
    Sets the stage axis position limits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        minPosition: c_int
        maxPosition: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    minPosition = c_int()
    maxPosition = c_int()

    output = SBC_SetStageAxisLimits(serial_number)

    return output


SBC_SetTriggerSwitches = lib.SBC_SetTriggerSwitches
SBC_SetTriggerSwitches.restype = c_short
SBC_SetTriggerSwitches.argtypes = []


def set_trigger_switches(serial_number):
    '''
    Sets the trigger switch parameter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        indicatorBits: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    indicatorBits = c_byte()

    output = SBC_SetTriggerSwitches(serial_number)

    return output


SBC_SetVelParams = lib.SBC_SetVelParams
SBC_SetVelParams.restype = c_short
SBC_SetVelParams.argtypes = []


def set_vel_params(serial_number):
    '''
    Sets the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_SetVelParams(serial_number)

    return output


SBC_SetVelParamsBlock = lib.SBC_SetVelParamsBlock
SBC_SetVelParamsBlock.restype = c_short
SBC_SetVelParamsBlock.argtypes = []


def set_vel_params_block(serial_number):
    '''
    Set the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocityParams: MOT_VelocityParameters
        velocityParameters: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()
    velocityParameters = MOT_VelocityParameters()

    output = SBC_SetVelParamsBlock(serial_number)

    return output


SBC_StartPolling = lib.SBC_StartPolling
SBC_StartPolling.restype = c_bool
SBC_StartPolling.argtypes = []


def start_polling(serial_number):
    '''
    Starts the internal polling loop which continuously requests position and status.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        milliseconds: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    milliseconds = c_int()

    output = SBC_StartPolling(serial_number)

    return output


SBC_StopImmediate = lib.SBC_StopImmediate
SBC_StopImmediate.restype = c_short
SBC_StopImmediate.argtypes = []


def stop_immediate(serial_number):
    '''
    Stop the current move immediately (with risk of losing track of position).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_StopImmediate(serial_number)

    return output


SBC_StopPolling = lib.SBC_StopPolling
SBC_StopPolling.restype = c_void_p
SBC_StopPolling.argtypes = []


def stop_polling(serial_number):
    '''
    Stops the internal polling loop.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_StopPolling(serial_number)

    return output


SBC_StopProfiled = lib.SBC_StopProfiled
SBC_StopProfiled.restype = c_short
SBC_StopProfiled.argtypes = []


def stop_profiled(serial_number):
    '''
    Stop the current move using the current velocity profile.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_StopProfiled(serial_number)

    return output


SBC_SuspendMoveMessages = lib.SBC_SuspendMoveMessages
SBC_SuspendMoveMessages.restype = c_short
SBC_SuspendMoveMessages.argtypes = []


def suspend_move_messages(serial_number):
    '''
    Suspend automatic messages at ends of moves.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = SBC_SuspendMoveMessages(serial_number)

    return output


