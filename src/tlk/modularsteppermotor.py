from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_float,
    c_int,
    c_int32,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    c_void_p,
    cdll)
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


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Modular.DLL")

SBC_CanHome = lib.SBC_CanHome
SBC_CanHome.restype = c_bool
SBC_CanHome.argtypes = [POINTER(c_char), c_short]


def can_home(serial_number, channel):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_CanHome(serial_number, channel)

    return output


SBC_CanMoveWithoutHomingFirst = lib.SBC_CanMoveWithoutHomingFirst
SBC_CanMoveWithoutHomingFirst.restype = c_bool
SBC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]


def can_move_without_homing_first(serial_number, channel):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_CanMoveWithoutHomingFirst(serial_number, channel)

    return output


SBC_DisableChannel = lib.SBC_DisableChannel
SBC_DisableChannel.restype = c_short
SBC_DisableChannel.argtypes = [POINTER(c_char), c_short]


def disable_channel(serial_number, channel):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_DisableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_EnableChannel = lib.SBC_EnableChannel
SBC_EnableChannel.restype = c_short
SBC_EnableChannel.argtypes = [POINTER(c_char), c_short]


def enable_channel(serial_number, channel):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_EnableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_EnableLastMsgTimer = lib.SBC_EnableLastMsgTimer
SBC_EnableLastMsgTimer.restype = c_void_p
SBC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]


def enable_last_msg_timer(serial_number, channel):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SBC_EnableLastMsgTimer(serial_number, channel, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


SBC_GetBacklash = lib.SBC_GetBacklash
SBC_GetBacklash.restype = c_long
SBC_GetBacklash.argtypes = [POINTER(c_char), c_short]


def get_backlash(serial_number, channel):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetBacklash(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetBowIndex = lib.SBC_GetBowIndex
SBC_GetBowIndex.restype = c_short
SBC_GetBowIndex.argtypes = [POINTER(c_char), c_short]


def get_bow_index(serial_number, channel):
    # Gets the stepper motor bow index.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetBowIndex(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetCalibrationFile = lib.SBC_GetCalibrationFile
SBC_GetCalibrationFile.restype = c_bool
SBC_GetCalibrationFile.argtypes = [POINTER(c_char), c_short, POINTER(c_char), c_short]


def get_calibration_file(serial_number, channel):
    # Get calibration file for this motor.

    serial_number = POINTER(c_char)
    channel = c_short()
    filename = POINTER(c_char)
    sizeOfBuffer = c_short()

    output = SBC_GetCalibrationFile(serial_number, channel, filename, sizeOfBuffer)

    return output


SBC_GetDeviceUnitFromRealValue = lib.SBC_GetDeviceUnitFromRealValue
SBC_GetDeviceUnitFromRealValue.restype = c_short
SBC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_short, c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number, channel):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    channel = c_short()
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = SBC_GetDeviceUnitFromRealValue(serial_number, channel, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


SBC_GetDigitalOutputs = lib.SBC_GetDigitalOutputs
SBC_GetDigitalOutputs.restype = c_byte
SBC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]


def get_digital_outputs(serial_number, channel):
    # Gets the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetDigitalOutputs(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetEncoderCounter = lib.SBC_GetEncoderCounter
SBC_GetEncoderCounter.restype = c_long
SBC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]


def get_encoder_counter(serial_number, channel):
    # Get the Encoder Counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetEncoderCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetHomingParamsBlock = lib.SBC_GetHomingParamsBlock
SBC_GetHomingParamsBlock.restype = c_short
SBC_GetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


def get_homing_params_block(serial_number, channel):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = SBC_GetHomingParamsBlock(serial_number, channel, homingParams)
    if output != 0:
        raise KinesisException(output)


SBC_GetHomingVelocity = lib.SBC_GetHomingVelocity
SBC_GetHomingVelocity.restype = c_uint
SBC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]


def get_homing_velocity(serial_number, channel):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetHomingVelocity(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetInputVoltage = lib.SBC_GetInputVoltage
SBC_GetInputVoltage.restype = c_long
SBC_GetInputVoltage.argtypes = [POINTER(c_char), c_short]


def get_input_voltage(serial_number, channel):
    # Gets the analogue input voltage reading.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetInputVoltage(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetJogMode = lib.SBC_GetJogMode
SBC_GetJogMode.restype = c_short
SBC_GetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number, channel):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SBC_GetJogMode(serial_number, channel, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


SBC_GetJogParamsBlock = lib.SBC_GetJogParamsBlock
SBC_GetJogParamsBlock.restype = c_short
SBC_GetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters, MOT_JogParameters]


def get_jog_params_block(serial_number, channel):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogParams = MOT_JogParameters()
    jogParameters = MOT_JogParameters()

    output = SBC_GetJogParamsBlock(serial_number, channel, jogParams, jogParameters)
    if output != 0:
        raise KinesisException(output)


SBC_GetJogStepSize = lib.SBC_GetJogStepSize
SBC_GetJogStepSize.restype = c_uint
SBC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]


def get_jog_step_size(serial_number, channel):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetJogStepSize(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetJogVelParams = lib.SBC_GetJogVelParams
SBC_GetJogVelParams.restype = c_short
SBC_GetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def get_jog_vel_params(serial_number, channel):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_GetJogVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SBC_GetJoystickParams = lib.SBC_GetJoystickParams
SBC_GetJoystickParams.restype = c_short
SBC_GetJoystickParams.argtypes = [POINTER(c_char), c_short, MOT_JoystickParameters]


def get_joystick_params(serial_number, channel):
    # Gets the joystick parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    joystickParams = MOT_JoystickParameters()

    output = SBC_GetJoystickParams(serial_number, channel, joystickParams)
    if output != 0:
        raise KinesisException(output)


SBC_GetLimitSwitchParams = lib.SBC_GetLimitSwitchParams
SBC_GetLimitSwitchParams.restype = c_short
SBC_GetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchModes,
    c_uint,
    c_uint,
    MOT_LimitSwitchSWModes]


def get_limit_switch_params(serial_number, channel):
    # Gets the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = SBC_GetLimitSwitchParams(
        serial_number,
        channel,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


SBC_GetLimitSwitchParamsBlock = lib.SBC_GetLimitSwitchParamsBlock
SBC_GetLimitSwitchParamsBlock.restype = c_short
SBC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LimitSwitchParameters]


def get_limit_switch_params_block(serial_number, channel):
    # Get the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SBC_GetLimitSwitchParamsBlock(serial_number, channel, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


SBC_GetMotorParams = lib.SBC_GetMotorParams
SBC_GetMotorParams.restype = c_short
SBC_GetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_float]


def get_motor_params(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SBC_GetMotorParams(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SBC_GetMotorParamsExt = lib.SBC_GetMotorParamsExt
SBC_GetMotorParamsExt.restype = c_short
SBC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]


def get_motor_params_ext(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SBC_GetMotorParamsExt(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SBC_GetMotorTravelLimits = lib.SBC_GetMotorTravelLimits
SBC_GetMotorTravelLimits.restype = c_short
SBC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def get_motor_travel_limits(serial_number, channel):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = SBC_GetMotorTravelLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


SBC_GetMotorTravelMode = lib.SBC_GetMotorTravelMode
SBC_GetMotorTravelMode.restype = MOT_TravelModes
SBC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]


def get_motor_travel_mode(serial_number, channel):
    # Get the motor travel mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetMotorTravelMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetMotorVelocityLimits = lib.SBC_GetMotorVelocityLimits
SBC_GetMotorVelocityLimits.restype = c_short
SBC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def get_motor_velocity_limits(serial_number, channel):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SBC_GetMotorVelocityLimits(serial_number, channel, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


SBC_GetMoveAbsolutePosition = lib.SBC_GetMoveAbsolutePosition
SBC_GetMoveAbsolutePosition.restype = c_int
SBC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


def get_move_absolute_position(serial_number, channel):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetMoveAbsolutePosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetMoveRelativeDistance = lib.SBC_GetMoveRelativeDistance
SBC_GetMoveRelativeDistance.restype = c_int
SBC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def get_move_relative_distance(serial_number, channel):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetMoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetNumberPositions = lib.SBC_GetNumberPositions
SBC_GetNumberPositions.restype = c_int
SBC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]


def get_number_positions(serial_number, channel):
    # Get number of positions.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetNumberPositions(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetPosition = lib.SBC_GetPosition
SBC_GetPosition.restype = c_int
SBC_GetPosition.argtypes = [POINTER(c_char), c_short]


def get_position(serial_number, channel):
    # Get the current position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetPositionCounter = lib.SBC_GetPositionCounter
SBC_GetPositionCounter.restype = c_long
SBC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]


def get_position_counter(serial_number, channel):
    # Get the Position Counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetPositionCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetPowerParams = lib.SBC_GetPowerParams
SBC_GetPowerParams.restype = c_short
SBC_GetPowerParams.argtypes = [POINTER(c_char), c_short, MOT_PowerParameters]


def get_power_params(serial_number, channel):
    # Sets the power parameters for the stepper motor.

    serial_number = POINTER(c_char)
    channel = c_short()
    powerParams = MOT_PowerParameters()

    output = SBC_GetPowerParams(serial_number, channel, powerParams)
    if output != 0:
        raise KinesisException(output)


SBC_GetRealValueFromDeviceUnit = lib.SBC_GetRealValueFromDeviceUnit
SBC_GetRealValueFromDeviceUnit.restype = c_short
SBC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_short, c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number, channel):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    channel = c_short()
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = SBC_GetRealValueFromDeviceUnit(serial_number, channel, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


SBC_GetSoftLimitMode = lib.SBC_GetSoftLimitMode
SBC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SBC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]


def get_soft_limit_mode(serial_number, channel):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetSoftLimitMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetStageAxisMaxPos = lib.SBC_GetStageAxisMaxPos
SBC_GetStageAxisMaxPos.restype = c_int
SBC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]


def get_stage_axis_max_pos(serial_number, channel):
    # Gets the Stepper Motor maximum stage position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetStageAxisMaxPos(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetStageAxisMinPos = lib.SBC_GetStageAxisMinPos
SBC_GetStageAxisMinPos.restype = c_int
SBC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]


def get_stage_axis_min_pos(serial_number, channel):
    # Gets the Stepper Motor minimum stage position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetStageAxisMinPos(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetStatusBits = lib.SBC_GetStatusBits
SBC_GetStatusBits.restype = c_ulong
SBC_GetStatusBits.argtypes = [POINTER(c_char), c_short]


def get_status_bits(serial_number, channel):
    # Get the current status bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetTriggerSwitches = lib.SBC_GetTriggerSwitches
SBC_GetTriggerSwitches.restype = c_byte
SBC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]


def get_trigger_switches(serial_number, channel):
    # Gets the trigger switch parameter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_GetTriggerSwitches(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_GetVelParams = lib.SBC_GetVelParams
SBC_GetVelParams.restype = c_short
SBC_GetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def get_vel_params(serial_number, channel):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_GetVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SBC_GetVelParamsBlock = lib.SBC_GetVelParamsBlock
SBC_GetVelParamsBlock.restype = c_short
SBC_GetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters, MOT_VelocityParameters]


def get_vel_params_block(serial_number, channel):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()
    velocityParameters = MOT_VelocityParameters()

    output = SBC_GetVelParamsBlock(serial_number, channel, velocityParams, velocityParameters)
    if output != 0:
        raise KinesisException(output)


SBC_HasLastMsgTimerOverrun = lib.SBC_HasLastMsgTimerOverrun
SBC_HasLastMsgTimerOverrun.restype = c_bool
SBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]


def has_last_msg_timer_overrun(serial_number, channel):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by SBC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_HasLastMsgTimerOverrun(serial_number, channel)

    return output


SBC_Home = lib.SBC_Home
SBC_Home.restype = c_short
SBC_Home.argtypes = [POINTER(c_char), c_short]


def home(serial_number, channel):
    # Home the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_Home(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_IsCalibrationActive = lib.SBC_IsCalibrationActive
SBC_IsCalibrationActive.restype = c_bool
SBC_IsCalibrationActive.argtypes = [POINTER(c_char), c_short]


def is_calibration_active(serial_number, channel):
    # Is a calibration file active for this motor.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_IsCalibrationActive(serial_number, channel)

    return output


SBC_MoveAbsolute = lib.SBC_MoveAbsolute
SBC_MoveAbsolute.restype = c_short
SBC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]


def move_absolute(serial_number, channel):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_MoveAbsolute(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_MoveAtVelocity = lib.SBC_MoveAtVelocity
SBC_MoveAtVelocity.restype = c_short
SBC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


def move_at_velocity(serial_number, channel):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    channel = c_short()
    direction = MOT_TravelDirection()

    output = SBC_MoveAtVelocity(serial_number, channel, direction)
    if output != 0:
        raise KinesisException(output)


SBC_MoveJog = lib.SBC_MoveJog
SBC_MoveJog.restype = c_short
SBC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


def move_jog(serial_number, channel):
    # Perform a jog.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogDirection = MOT_TravelDirection()

    output = SBC_MoveJog(serial_number, channel, jogDirection)
    if output != 0:
        raise KinesisException(output)


SBC_MoveRelative = lib.SBC_MoveRelative
SBC_MoveRelative.restype = c_short
SBC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]


def move_relative(serial_number, channel):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    channel = c_short()
    displacement = c_int()

    output = SBC_MoveRelative(serial_number, channel, displacement)
    if output != 0:
        raise KinesisException(output)


SBC_MoveRelativeDistance = lib.SBC_MoveRelativeDistance
SBC_MoveRelativeDistance.restype = c_short
SBC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def move_relative_distance(serial_number, channel):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_MoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_MoveToPosition = lib.SBC_MoveToPosition
SBC_MoveToPosition.restype = c_short
SBC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]


def move_to_position(serial_number, channel):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    channel = c_short()
    index = c_int()

    output = SBC_MoveToPosition(serial_number, channel, index)
    if output != 0:
        raise KinesisException(output)


SBC_NeedsHoming = lib.SBC_NeedsHoming
SBC_NeedsHoming.restype = c_bool
SBC_NeedsHoming.argtypes = [POINTER(c_char), c_short]


def needs_homing(serial_number, channel):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_NeedsHoming(serial_number, channel)

    return output


SBC_PollingDuration = lib.SBC_PollingDuration
SBC_PollingDuration.restype = c_long
SBC_PollingDuration.argtypes = [POINTER(c_char), c_short]


def polling_duration(serial_number, channel):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_PollingDuration(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_RequestDigitalOutputs = lib.SBC_RequestDigitalOutputs
SBC_RequestDigitalOutputs.restype = c_short
SBC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]


def request_digital_outputs(serial_number, channel):
    # Requests the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_RequestDigitalOutputs(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_RequestInputVoltage = lib.SBC_RequestInputVoltage
SBC_RequestInputVoltage.restype = c_short
SBC_RequestInputVoltage.argtypes = [POINTER(c_char), c_short]


def request_input_voltage(serial_number, channel):
    # Requests the analogue input voltage reading.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_RequestInputVoltage(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_RequestPosition = lib.SBC_RequestPosition
SBC_RequestPosition.restype = c_short
SBC_RequestPosition.argtypes = [POINTER(c_char), c_short]


def request_position(serial_number, channel):
    # Requests the current position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_RequestPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_RequestSettings = lib.SBC_RequestSettings
SBC_RequestSettings.restype = c_short
SBC_RequestSettings.argtypes = [POINTER(c_char), c_short]


def request_settings(serial_number, channel):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_RequestSettings(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_RequestStatusBits = lib.SBC_RequestStatusBits
SBC_RequestStatusBits.restype = c_short
SBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]


def request_status_bits(serial_number, channel):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_RequestStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_ResetRotationModes = lib.SBC_ResetRotationModes
SBC_ResetRotationModes.restype = c_short
SBC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]


def reset_rotation_modes(serial_number, channel):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_ResetRotationModes(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_ResumeMoveMessages = lib.SBC_ResumeMoveMessages
SBC_ResumeMoveMessages.restype = c_short
SBC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]


def resume_move_messages(serial_number, channel):
    # Resume suspended move messages.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_ResumeMoveMessages(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_SetBacklash = lib.SBC_SetBacklash
SBC_SetBacklash.restype = c_short
SBC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]


def set_backlash(serial_number, channel):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    channel = c_short()
    distance = c_long()

    output = SBC_SetBacklash(serial_number, channel, distance)
    if output != 0:
        raise KinesisException(output)


SBC_SetBowIndex = lib.SBC_SetBowIndex
SBC_SetBowIndex.restype = c_short
SBC_SetBowIndex.argtypes = [POINTER(c_char), c_short, c_short]


def set_bow_index(serial_number, channel):
    # Sets the stepper motor bow index.

    serial_number = POINTER(c_char)
    channel = c_short()
    bowIndex = c_short()

    output = SBC_SetBowIndex(serial_number, channel, bowIndex)
    if output != 0:
        raise KinesisException(output)


SBC_SetCalibrationFile = lib.SBC_SetCalibrationFile
SBC_SetCalibrationFile.restype = c_void_p
SBC_SetCalibrationFile.argtypes = [POINTER(c_char), c_short, POINTER(c_char), c_bool]


def set_calibration_file(serial_number, channel):
    # Set the calibration file for this motor.

    serial_number = POINTER(c_char)
    channel = c_short()
    filename = POINTER(c_char)
    enabled = c_bool()

    output = SBC_SetCalibrationFile(serial_number, channel, filename, enabled)
    if output != 0:
        raise KinesisException(output)


SBC_SetDigitalOutputs = lib.SBC_SetDigitalOutputs
SBC_SetDigitalOutputs.restype = c_short
SBC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]


def set_digital_outputs(serial_number, channel):
    # Sets the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()
    outputsBits = c_byte()

    output = SBC_SetDigitalOutputs(serial_number, channel, outputsBits)
    if output != 0:
        raise KinesisException(output)


SBC_SetDirection = lib.SBC_SetDirection
SBC_SetDirection.restype = c_short
SBC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]


def set_direction(serial_number, channel):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    channel = c_short()
    reverse = c_bool()

    output = SBC_SetDirection(serial_number, channel, reverse)
    if output != 0:
        raise KinesisException(output)


SBC_SetEncoderCounter = lib.SBC_SetEncoderCounter
SBC_SetEncoderCounter.restype = c_short
SBC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]


def set_encoder_counter(serial_number, channel):
    # Set the Encoder Counter values.

    serial_number = POINTER(c_char)
    channel = c_short()
    count = c_long()

    output = SBC_SetEncoderCounter(serial_number, channel, count)
    if output != 0:
        raise KinesisException(output)


SBC_SetHomingParamsBlock = lib.SBC_SetHomingParamsBlock
SBC_SetHomingParamsBlock.restype = c_short
SBC_SetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


def set_homing_params_block(serial_number, channel):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = SBC_SetHomingParamsBlock(serial_number, channel, homingParams)
    if output != 0:
        raise KinesisException(output)


SBC_SetHomingVelocity = lib.SBC_SetHomingVelocity
SBC_SetHomingVelocity.restype = c_short
SBC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]


def set_homing_velocity(serial_number, channel):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocity = c_uint()

    output = SBC_SetHomingVelocity(serial_number, channel, velocity)
    if output != 0:
        raise KinesisException(output)


SBC_SetJogMode = lib.SBC_SetJogMode
SBC_SetJogMode.restype = c_short
SBC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number, channel):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SBC_SetJogMode(serial_number, channel, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


SBC_SetJogParamsBlock = lib.SBC_SetJogParamsBlock
SBC_SetJogParamsBlock.restype = c_short
SBC_SetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters, MOT_JogParameters]


def set_jog_params_block(serial_number, channel):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogParams = MOT_JogParameters()
    jogParameters = MOT_JogParameters()

    output = SBC_SetJogParamsBlock(serial_number, channel, jogParams, jogParameters)
    if output != 0:
        raise KinesisException(output)


SBC_SetJogStepSize = lib.SBC_SetJogStepSize
SBC_SetJogStepSize.restype = c_short
SBC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]


def set_jog_step_size(serial_number, channel):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepSize = c_uint()

    output = SBC_SetJogStepSize(serial_number, channel, stepSize)
    if output != 0:
        raise KinesisException(output)


SBC_SetJogVelParams = lib.SBC_SetJogVelParams
SBC_SetJogVelParams.restype = c_short
SBC_SetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_jog_vel_params(serial_number, channel):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_SetJogVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SBC_SetJoystickParams = lib.SBC_SetJoystickParams
SBC_SetJoystickParams.restype = c_short
SBC_SetJoystickParams.argtypes = [POINTER(c_char), c_short, MOT_JoystickParameters]


def set_joystick_params(serial_number, channel):
    # Sets the joystick parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    joystickParams = MOT_JoystickParameters()

    output = SBC_SetJoystickParams(serial_number, channel, joystickParams)
    if output != 0:
        raise KinesisException(output)


SBC_SetLimitSwitchParams = lib.SBC_SetLimitSwitchParams
SBC_SetLimitSwitchParams.restype = c_short
SBC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchModes,
    c_uint,
    c_uint,
    MOT_LimitSwitchSWModes]


def set_limit_switch_params(serial_number, channel):
    # Sets the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = SBC_SetLimitSwitchParams(
        serial_number,
        channel,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


SBC_SetLimitSwitchParamsBlock = lib.SBC_SetLimitSwitchParamsBlock
SBC_SetLimitSwitchParamsBlock.restype = c_short
SBC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LimitSwitchParameters]


def set_limit_switch_params_block(serial_number, channel):
    # Set the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SBC_SetLimitSwitchParamsBlock(serial_number, channel, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


SBC_SetLimitsSoftwareApproachPolicy = lib.SBC_SetLimitsSoftwareApproachPolicy
SBC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SBC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number, channel):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = SBC_SetLimitsSoftwareApproachPolicy(serial_number, channel, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


SBC_SetMotorParams = lib.SBC_SetMotorParams
SBC_SetMotorParams.restype = c_short
SBC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_float]


def set_motor_params(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SBC_SetMotorParams(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SBC_SetMotorParamsExt = lib.SBC_SetMotorParamsExt
SBC_SetMotorParamsExt.restype = c_short
SBC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]


def set_motor_params_ext(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SBC_SetMotorParamsExt(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SBC_SetMotorTravelLimits = lib.SBC_SetMotorTravelLimits
SBC_SetMotorTravelLimits.restype = c_short
SBC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def set_motor_travel_limits(serial_number, channel):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = SBC_SetMotorTravelLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


SBC_SetMotorTravelMode = lib.SBC_SetMotorTravelMode
SBC_SetMotorTravelMode.restype = c_short
SBC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]


def set_motor_travel_mode(serial_number, channel):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    travelMode = MOT_TravelModes()

    output = SBC_SetMotorTravelMode(serial_number, channel, travelMode)
    if output != 0:
        raise KinesisException(output)


SBC_SetMotorVelocityLimits = lib.SBC_SetMotorVelocityLimits
SBC_SetMotorVelocityLimits.restype = c_short
SBC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def set_motor_velocity_limits(serial_number, channel):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SBC_SetMotorVelocityLimits(serial_number, channel, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


SBC_SetMoveAbsolutePosition = lib.SBC_SetMoveAbsolutePosition
SBC_SetMoveAbsolutePosition.restype = c_short
SBC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]


def set_move_absolute_position(serial_number, channel):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    channel = c_short()
    position = c_int()

    output = SBC_SetMoveAbsolutePosition(serial_number, channel, position)
    if output != 0:
        raise KinesisException(output)


SBC_SetMoveRelativeDistance = lib.SBC_SetMoveRelativeDistance
SBC_SetMoveRelativeDistance.restype = c_short
SBC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]


def set_move_relative_distance(serial_number, channel):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    channel = c_short()
    distance = c_int()

    output = SBC_SetMoveRelativeDistance(serial_number, channel, distance)
    if output != 0:
        raise KinesisException(output)


SBC_SetPositionCounter = lib.SBC_SetPositionCounter
SBC_SetPositionCounter.restype = c_short
SBC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]


def set_position_counter(serial_number, channel):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    channel = c_short()
    count = c_long()

    output = SBC_SetPositionCounter(serial_number, channel, count)
    if output != 0:
        raise KinesisException(output)


SBC_SetPowerParams = lib.SBC_SetPowerParams
SBC_SetPowerParams.restype = c_short
SBC_SetPowerParams.argtypes = [POINTER(c_char), c_short, MOT_PowerParameters]


def set_power_params(serial_number, channel):
    # Sets the power parameters for the stepper motor.

    serial_number = POINTER(c_char)
    channel = c_short()
    powerParams = MOT_PowerParameters()

    output = SBC_SetPowerParams(serial_number, channel, powerParams)
    if output != 0:
        raise KinesisException(output)


SBC_SetRotationModes = lib.SBC_SetRotationModes
SBC_SetRotationModes.restype = c_short
SBC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number, channel):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = SBC_SetRotationModes(serial_number, channel, mode, direction)
    if output != 0:
        raise KinesisException(output)


SBC_SetStageAxisLimits = lib.SBC_SetStageAxisLimits
SBC_SetStageAxisLimits.restype = c_short
SBC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_stage_axis_limits(serial_number, channel):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_int()
    maxPosition = c_int()

    output = SBC_SetStageAxisLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


SBC_SetTriggerSwitches = lib.SBC_SetTriggerSwitches
SBC_SetTriggerSwitches.restype = c_short
SBC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]


def set_trigger_switches(serial_number, channel):
    # Sets the trigger switch parameter.

    serial_number = POINTER(c_char)
    channel = c_short()
    indicatorBits = c_byte()

    output = SBC_SetTriggerSwitches(serial_number, channel, indicatorBits)
    if output != 0:
        raise KinesisException(output)


SBC_SetVelParams = lib.SBC_SetVelParams
SBC_SetVelParams.restype = c_short
SBC_SetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_vel_params(serial_number, channel):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_SetVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SBC_SetVelParamsBlock = lib.SBC_SetVelParamsBlock
SBC_SetVelParamsBlock.restype = c_short
SBC_SetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters, MOT_VelocityParameters]


def set_vel_params_block(serial_number, channel):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()
    velocityParameters = MOT_VelocityParameters()

    output = SBC_SetVelParamsBlock(serial_number, channel, velocityParams, velocityParameters)
    if output != 0:
        raise KinesisException(output)


SBC_StartPolling = lib.SBC_StartPolling
SBC_StartPolling.restype = c_bool
SBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]


def start_polling(serial_number, channel):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    channel = c_short()
    milliseconds = c_int()

    output = SBC_StartPolling(serial_number, channel, milliseconds)

    return output


SBC_StopImmediate = lib.SBC_StopImmediate
SBC_StopImmediate.restype = c_short
SBC_StopImmediate.argtypes = [POINTER(c_char), c_short]


def stop_immediate(serial_number, channel):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_StopImmediate(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_StopPolling = lib.SBC_StopPolling
SBC_StopPolling.restype = c_void_p
SBC_StopPolling.argtypes = [POINTER(c_char), c_short]


def stop_polling(serial_number, channel):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_StopPolling(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_StopProfiled = lib.SBC_StopProfiled
SBC_StopProfiled.restype = c_short
SBC_StopProfiled.argtypes = [POINTER(c_char), c_short]


def stop_profiled(serial_number, channel):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_StopProfiled(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


SBC_SuspendMoveMessages = lib.SBC_SuspendMoveMessages
SBC_SuspendMoveMessages.restype = c_short
SBC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]


def suspend_move_messages(serial_number, channel):
    # Suspend automatic messages at ends of moves.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = SBC_SuspendMoveMessages(serial_number, channel)
    if output != 0:
        raise KinesisException(output)
