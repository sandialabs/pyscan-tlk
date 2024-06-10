from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_double,
    c_float,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    MOT_ButtonModes,
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
    MOT_ButtonParameters,
    MOT_DC_PIDParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.DCServo.DLL")

CC_CanHome = lib.CC_CanHome
CC_CanHome.restype = c_bool
CC_CanHome.argtypes = [POINTER(c_char)]


def can_home(serial_number):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)

    output = CC_CanHome(serial_number)

    return output


CC_CanMoveWithoutHomingFirst = lib.CC_CanMoveWithoutHomingFirst
CC_CanMoveWithoutHomingFirst.restype = c_bool
CC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


def can_move_without_homing_first(serial_number):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)

    output = CC_CanMoveWithoutHomingFirst(serial_number)

    return output


CC_CheckConnection = lib.CC_CheckConnection
CC_CheckConnection.restype = c_bool
CC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = CC_CheckConnection(serial_number)

    return output


CC_ClearMessageQueue = lib.CC_ClearMessageQueue
CC_ClearMessageQueue.restype = c_void_p
CC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = CC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_Close = lib.CC_Close
CC_Close.restype = c_void_p
CC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = CC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_DisableChannel = lib.CC_DisableChannel
CC_DisableChannel.restype = c_short
CC_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel(serial_number):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)

    output = CC_DisableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_EnableChannel = lib.CC_EnableChannel
CC_EnableChannel.restype = c_short
CC_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel(serial_number):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)

    output = CC_EnableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_EnableLastMsgTimer = lib.CC_EnableLastMsgTimer
CC_EnableLastMsgTimer.restype = c_void_p
CC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = CC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


CC_GetBacklash = lib.CC_GetBacklash
CC_GetBacklash.restype = c_long
CC_GetBacklash.argtypes = [POINTER(c_char)]


def get_backlash(serial_number):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)

    output = CC_GetBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetButtonParams = lib.CC_GetButtonParams
CC_GetButtonParams.restype = c_short
CC_GetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int, c_short]


def get_button_params(serial_number):
    # Gets the TCube button parameters.

    serial_number = POINTER(c_char)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()
    timeout = c_short()

    output = CC_GetButtonParams(serial_number, buttonMode, leftButtonPosition, rightButtonPosition, timeout)
    if output != 0:
        raise KinesisException(output)


CC_GetButtonParamsBlock = lib.CC_GetButtonParamsBlock
CC_GetButtonParamsBlock.restype = c_short
CC_GetButtonParamsBlock.argtypes = [POINTER(c_char), MOT_ButtonParameters]


def get_button_params_block(serial_number):
    # Get the button parameters.

    serial_number = POINTER(c_char)
    buttonParams = MOT_ButtonParameters()

    output = CC_GetButtonParamsBlock(serial_number, buttonParams)
    if output != 0:
        raise KinesisException(output)


CC_GetDCPIDParams = lib.CC_GetDCPIDParams
CC_GetDCPIDParams.restype = c_short
CC_GetDCPIDParams.argtypes = [POINTER(c_char), MOT_DC_PIDParameters]


def get_d_c_p_i_d_params(serial_number):
    # Get the DC PID parameters.

    serial_number = POINTER(c_char)
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()

    output = CC_GetDCPIDParams(serial_number, DCproportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


CC_GetDeviceUnitFromRealValue = lib.CC_GetDeviceUnitFromRealValue
CC_GetDeviceUnitFromRealValue.restype = c_short
CC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = CC_GetDeviceUnitFromRealValue(serial_number, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


CC_GetEncoderCounter = lib.CC_GetEncoderCounter
CC_GetEncoderCounter.restype = c_long
CC_GetEncoderCounter.argtypes = [POINTER(c_char)]


def get_encoder_counter(serial_number):
    # Get the Encoder Counter.

    serial_number = POINTER(c_char)

    output = CC_GetEncoderCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetHardwareInfo = lib.CC_GetHardwareInfo
CC_GetHardwareInfo.restype = c_short
CC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]


def get_hardware_info(serial_number):
    # Gets the hardware information from the device.

    serial_number = POINTER(c_char)
    modelNo = POINTER(c_char)
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = CC_GetHardwareInfo(
        serial_number,
        modelNo,
        sizeOfModelNo,
        type,
        numChannels,
        notes,
        sizeOfNotes,
        firmwareVersion,
        hardwareVersion,
        modificationState)
    if output != 0:
        raise KinesisException(output)


CC_GetHardwareInfoBlock = lib.CC_GetHardwareInfoBlock
CC_GetHardwareInfoBlock.restype = c_short
CC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = CC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


CC_GetHomingParamsBlock = lib.CC_GetHomingParamsBlock
CC_GetHomingParamsBlock.restype = c_short
CC_GetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def get_homing_params_block(serial_number):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = CC_GetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


CC_GetHomingVelocity = lib.CC_GetHomingVelocity
CC_GetHomingVelocity.restype = c_uint
CC_GetHomingVelocity.argtypes = [POINTER(c_char)]


def get_homing_velocity(serial_number):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)

    output = CC_GetHomingVelocity(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetHubBay = lib.CC_GetHubBay
CC_GetHubBay.restype = POINTER(c_char)
CC_GetHubBay.argtypes = [POINTER(c_char)]


def get_hub_bay(serial_number):
    # Gets the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = CC_GetHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetJogMode = lib.CC_GetJogMode
CC_GetJogMode.restype = c_short
CC_GetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = CC_GetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


CC_GetJogParamsBlock = lib.CC_GetJogParamsBlock
CC_GetJogParamsBlock.restype = c_short
CC_GetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def get_jog_params_block(serial_number):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = CC_GetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


CC_GetJogStepSize = lib.CC_GetJogStepSize
CC_GetJogStepSize.restype = c_uint
CC_GetJogStepSize.argtypes = [POINTER(c_char)]


def get_jog_step_size(serial_number):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)

    output = CC_GetJogStepSize(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetJogVelParams = lib.CC_GetJogVelParams
CC_GetJogVelParams.restype = c_short
CC_GetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_jog_vel_params(serial_number):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_GetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


CC_GetLEDswitches = lib.CC_GetLEDswitches
CC_GetLEDswitches.restype = c_long
CC_GetLEDswitches.argtypes = [POINTER(c_char)]


def get_l_e_dswitches(serial_number):
    # Get the LED indicator bits on cube.

    serial_number = POINTER(c_char)

    output = CC_GetLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetLimitSwitchParams = lib.CC_GetLimitSwitchParams
CC_GetLimitSwitchParams.restype = c_short
CC_GetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    MOT_LimitSwitchModes,
    c_uint,
    c_uint,
    MOT_LimitSwitchSWModes]


def get_limit_switch_params(serial_number):
    # Gets the limit switch parameters.

    serial_number = POINTER(c_char)
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = CC_GetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


CC_GetLimitSwitchParamsBlock = lib.CC_GetLimitSwitchParamsBlock
CC_GetLimitSwitchParamsBlock.restype = c_short
CC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def get_limit_switch_params_block(serial_number):
    # Get the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = CC_GetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


CC_GetMotorParams = lib.CC_GetMotorParams
CC_GetMotorParams.restype = c_short
CC_GetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def get_motor_params(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = CC_GetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


CC_GetMotorParamsExt = lib.CC_GetMotorParamsExt
CC_GetMotorParamsExt.restype = c_short
CC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def get_motor_params_ext(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = CC_GetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


CC_GetMotorTravelLimits = lib.CC_GetMotorTravelLimits
CC_GetMotorTravelLimits.restype = c_short
CC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_travel_limits(serial_number):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = CC_GetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


CC_GetMotorTravelMode = lib.CC_GetMotorTravelMode
CC_GetMotorTravelMode.restype = MOT_TravelModes
CC_GetMotorTravelMode.argtypes = [POINTER(c_char)]


def get_motor_travel_mode(serial_number):
    # Get the motor travel mode.

    serial_number = POINTER(c_char)

    output = CC_GetMotorTravelMode(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetMotorVelocityLimits = lib.CC_GetMotorVelocityLimits
CC_GetMotorVelocityLimits.restype = c_short
CC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_velocity_limits(serial_number):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = CC_GetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


CC_GetMoveAbsolutePosition = lib.CC_GetMoveAbsolutePosition
CC_GetMoveAbsolutePosition.restype = c_int
CC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def get_move_absolute_position(serial_number):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)

    output = CC_GetMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetMoveRelativeDistance = lib.CC_GetMoveRelativeDistance
CC_GetMoveRelativeDistance.restype = c_int
CC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


def get_move_relative_distance(serial_number):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)

    output = CC_GetMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetNextMessage = lib.CC_GetNextMessage
CC_GetNextMessage.restype = c_bool
CC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = CC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


CC_GetNumberPositions = lib.CC_GetNumberPositions
CC_GetNumberPositions.restype = c_int
CC_GetNumberPositions.argtypes = [POINTER(c_char)]


def get_number_positions(serial_number):
    # Get number of positions.

    serial_number = POINTER(c_char)

    output = CC_GetNumberPositions(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetPosition = lib.CC_GetPosition
CC_GetPosition.restype = c_int
CC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)

    output = CC_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetPositionCounter = lib.CC_GetPositionCounter
CC_GetPositionCounter.restype = c_long
CC_GetPositionCounter.argtypes = [POINTER(c_char)]


def get_position_counter(serial_number):
    # Get the Position Counter.

    serial_number = POINTER(c_char)

    output = CC_GetPositionCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetPotentiometerParams = lib.CC_GetPotentiometerParams
CC_GetPotentiometerParams.restype = c_short
CC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]


def get_potentiometer_params(serial_number):
    # Gets the potentiometer parameters for the TCube.

    serial_number = POINTER(c_char)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = CC_GetPotentiometerParams(serial_number, index, thresholdDeflection, velocity)
    if output != 0:
        raise KinesisException(output)


CC_GetPotentiometerParamsBlock = lib.CC_GetPotentiometerParamsBlock
CC_GetPotentiometerParamsBlock.restype = c_short
CC_GetPotentiometerParamsBlock.argtypes = [POINTER(c_char), MOT_PotentiometerSteps]


def get_potentiometer_params_block(serial_number):
    # Get the potentiometer parameters.

    serial_number = POINTER(c_char)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = CC_GetPotentiometerParamsBlock(serial_number, potentiometerSteps)
    if output != 0:
        raise KinesisException(output)


CC_GetRealValueFromDeviceUnit = lib.CC_GetRealValueFromDeviceUnit
CC_GetRealValueFromDeviceUnit.restype = c_short
CC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = CC_GetRealValueFromDeviceUnit(serial_number, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


CC_GetSoftLimitMode = lib.CC_GetSoftLimitMode
CC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
CC_GetSoftLimitMode.argtypes = [POINTER(c_char)]


def get_soft_limit_mode(serial_number):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)

    output = CC_GetSoftLimitMode(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetSoftwareVersion = lib.CC_GetSoftwareVersion
CC_GetSoftwareVersion.restype = c_ulong
CC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = CC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetStageAxisMaxPos = lib.CC_GetStageAxisMaxPos
CC_GetStageAxisMaxPos.restype = c_int
CC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


def get_stage_axis_max_pos(serial_number):
    # Gets the DC Motor maximum stage position.

    serial_number = POINTER(c_char)

    output = CC_GetStageAxisMaxPos(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetStageAxisMinPos = lib.CC_GetStageAxisMinPos
CC_GetStageAxisMinPos.restype = c_int
CC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


def get_stage_axis_min_pos(serial_number):
    # Gets the DC Motor minimum stage position.

    serial_number = POINTER(c_char)

    output = CC_GetStageAxisMinPos(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetStatusBits = lib.CC_GetStatusBits
CC_GetStatusBits.restype = c_ulong
CC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = CC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_GetVelParams = lib.CC_GetVelParams
CC_GetVelParams.restype = c_short
CC_GetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_vel_params(serial_number):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_GetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


CC_GetVelParamsBlock = lib.CC_GetVelParamsBlock
CC_GetVelParamsBlock.restype = c_short
CC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def get_vel_params_block(serial_number):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = CC_GetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


CC_HasLastMsgTimerOverrun = lib.CC_HasLastMsgTimerOverrun
CC_HasLastMsgTimerOverrun.restype = c_bool
CC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by CC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = CC_HasLastMsgTimerOverrun(serial_number)

    return output


CC_Home = lib.CC_Home
CC_Home.restype = c_short
CC_Home.argtypes = [POINTER(c_char)]


def home(serial_number):
    # Home the device.

    serial_number = POINTER(c_char)

    output = CC_Home(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_Identify = lib.CC_Identify
CC_Identify.restype = c_void_p
CC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = CC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_LoadNamedSettings = lib.CC_LoadNamedSettings
CC_LoadNamedSettings.restype = c_bool
CC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = CC_LoadNamedSettings(serial_number, settingsName)

    return output


CC_LoadSettings = lib.CC_LoadSettings
CC_LoadSettings.restype = c_bool
CC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = CC_LoadSettings(serial_number)

    return output


CC_MessageQueueSize = lib.CC_MessageQueueSize
CC_MessageQueueSize.restype = c_int
CC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = CC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_MoveAbsolute = lib.CC_MoveAbsolute
CC_MoveAbsolute.restype = c_short
CC_MoveAbsolute.argtypes = [POINTER(c_char)]


def move_absolute(serial_number):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)

    output = CC_MoveAbsolute(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_MoveAtVelocity = lib.CC_MoveAtVelocity
CC_MoveAtVelocity.restype = c_short
CC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_at_velocity(serial_number):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    direction = MOT_TravelDirection()

    output = CC_MoveAtVelocity(serial_number, direction)
    if output != 0:
        raise KinesisException(output)


CC_MoveJog = lib.CC_MoveJog
CC_MoveJog.restype = c_short
CC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_jog(serial_number):
    # Perform a jog.

    serial_number = POINTER(c_char)
    jogDirection = MOT_TravelDirection()

    output = CC_MoveJog(serial_number, jogDirection)
    if output != 0:
        raise KinesisException(output)


CC_MoveRelative = lib.CC_MoveRelative
CC_MoveRelative.restype = c_short
CC_MoveRelative.argtypes = [POINTER(c_char), c_int]


def move_relative(serial_number):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    displacement = c_int()

    output = CC_MoveRelative(serial_number, displacement)
    if output != 0:
        raise KinesisException(output)


CC_MoveRelativeDistance = lib.CC_MoveRelativeDistance
CC_MoveRelativeDistance.restype = c_short
CC_MoveRelativeDistance.argtypes = [POINTER(c_char)]


def move_relative_distance(serial_number):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)

    output = CC_MoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_MoveToPosition = lib.CC_MoveToPosition
CC_MoveToPosition.restype = c_short
CC_MoveToPosition.argtypes = [POINTER(c_char), c_int]


def move_to_position(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    index = c_int()

    output = CC_MoveToPosition(serial_number, index)
    if output != 0:
        raise KinesisException(output)


CC_NeedsHoming = lib.CC_NeedsHoming
CC_NeedsHoming.restype = c_bool
CC_NeedsHoming.argtypes = [POINTER(c_char)]


def needs_homing(serial_number):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)

    output = CC_NeedsHoming(serial_number)

    return output


CC_Open = lib.CC_Open
CC_Open.restype = c_short
CC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = CC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_PersistSettings = lib.CC_PersistSettings
CC_PersistSettings.restype = c_bool
CC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = CC_PersistSettings(serial_number)

    return output


CC_PollingDuration = lib.CC_PollingDuration
CC_PollingDuration.restype = c_long
CC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = CC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RegisterMessageCallback = lib.CC_RegisterMessageCallback
CC_RegisterMessageCallback.restype = c_void_p
CC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = CC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


CC_RequestBacklash = lib.CC_RequestBacklash
CC_RequestBacklash.restype = c_short
CC_RequestBacklash.argtypes = [POINTER(c_char)]


def request_backlash(serial_number):
    # Requests the backlash.

    serial_number = POINTER(c_char)

    output = CC_RequestBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestButtonParams = lib.CC_RequestButtonParams
CC_RequestButtonParams.restype = c_short
CC_RequestButtonParams.argtypes = [POINTER(c_char)]


def request_button_params(serial_number):
    # Requests the button parameters.

    serial_number = POINTER(c_char)

    output = CC_RequestButtonParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestDCPIDParams = lib.CC_RequestDCPIDParams
CC_RequestDCPIDParams.restype = c_short
CC_RequestDCPIDParams.argtypes = [POINTER(c_char)]


def request_d_c_p_i_d_params(serial_number):
    # Requests the PID parameters for DC motors used in an algorithm involving calculus.

    serial_number = POINTER(c_char)

    output = CC_RequestDCPIDParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestEncoderCounter = lib.CC_RequestEncoderCounter
CC_RequestEncoderCounter.restype = c_short
CC_RequestEncoderCounter.argtypes = [POINTER(c_char)]


def request_encoder_counter(serial_number):
    # Requests the encoder counter.

    serial_number = POINTER(c_char)

    output = CC_RequestEncoderCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestHomingParams = lib.CC_RequestHomingParams
CC_RequestHomingParams.restype = c_short
CC_RequestHomingParams.argtypes = [POINTER(c_char)]


def request_homing_params(serial_number):
    # Requests the homing parameters.

    serial_number = POINTER(c_char)

    output = CC_RequestHomingParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestJogParams = lib.CC_RequestJogParams
CC_RequestJogParams.restype = c_short
CC_RequestJogParams.argtypes = [POINTER(c_char)]


def request_jog_params(serial_number):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)

    output = CC_RequestJogParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestLEDswitches = lib.CC_RequestLEDswitches
CC_RequestLEDswitches.restype = c_short
CC_RequestLEDswitches.argtypes = [POINTER(c_char)]


def request_l_e_dswitches(serial_number):
    # Request the LED indicator bits on cube.

    serial_number = POINTER(c_char)

    output = CC_RequestLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestLimitSwitchParams = lib.CC_RequestLimitSwitchParams
CC_RequestLimitSwitchParams.restype = c_short
CC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]


def request_limit_switch_params(serial_number):
    # Requests the limit switch parameters.

    serial_number = POINTER(c_char)

    output = CC_RequestLimitSwitchParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestMoveAbsolutePosition = lib.CC_RequestMoveAbsolutePosition
CC_RequestMoveAbsolutePosition.restype = c_short
CC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def request_move_absolute_position(serial_number):
    # Requests the position of next absolute move.

    serial_number = POINTER(c_char)

    output = CC_RequestMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestMoveRelativeDistance = lib.CC_RequestMoveRelativeDistance
CC_RequestMoveRelativeDistance.restype = c_short
CC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


def request_move_relative_distance(serial_number):
    # Requests the move relative distance.

    serial_number = POINTER(c_char)

    output = CC_RequestMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestPosition = lib.CC_RequestPosition
CC_RequestPosition.restype = c_short
CC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current position.

    serial_number = POINTER(c_char)

    output = CC_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestPotentiometerParams = lib.CC_RequestPotentiometerParams
CC_RequestPotentiometerParams.restype = c_short
CC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]


def request_potentiometer_params(serial_number):
    # Requests the potentiometer parameters.

    serial_number = POINTER(c_char)

    output = CC_RequestPotentiometerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestSettings = lib.CC_RequestSettings
CC_RequestSettings.restype = c_short
CC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = CC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestStatusBits = lib.CC_RequestStatusBits
CC_RequestStatusBits.restype = c_short
CC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)

    output = CC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_RequestVelParams = lib.CC_RequestVelParams
CC_RequestVelParams.restype = c_short
CC_RequestVelParams.argtypes = [POINTER(c_char)]


def request_vel_params(serial_number):
    # Requests the move velocity parameters.

    serial_number = POINTER(c_char)

    output = CC_RequestVelParams(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_ResetRotationModes = lib.CC_ResetRotationModes
CC_ResetRotationModes.restype = c_short
CC_ResetRotationModes.argtypes = [POINTER(c_char)]


def reset_rotation_modes(serial_number):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)

    output = CC_ResetRotationModes(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_ResumeMoveMessages = lib.CC_ResumeMoveMessages
CC_ResumeMoveMessages.restype = c_short
CC_ResumeMoveMessages.argtypes = [POINTER(c_char)]


def resume_move_messages(serial_number):
    # Resume suspended move messages.

    serial_number = POINTER(c_char)

    output = CC_ResumeMoveMessages(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_SetBacklash = lib.CC_SetBacklash
CC_SetBacklash.restype = c_short
CC_SetBacklash.argtypes = [POINTER(c_char), c_long]


def set_backlash(serial_number):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    distance = c_long()

    output = CC_SetBacklash(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


CC_SetButtonParams = lib.CC_SetButtonParams
CC_SetButtonParams.restype = c_short
CC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]


def set_button_params(serial_number):
    # Sets the TCube button parameters.

    serial_number = POINTER(c_char)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()

    output = CC_SetButtonParams(serial_number, buttonMode, leftButtonPosition, rightButtonPosition)
    if output != 0:
        raise KinesisException(output)


CC_SetButtonParamsBlock = lib.CC_SetButtonParamsBlock
CC_SetButtonParamsBlock.restype = c_short
CC_SetButtonParamsBlock.argtypes = [POINTER(c_char), MOT_ButtonParameters]


def set_button_params_block(serial_number):
    # Set the button parameters.

    serial_number = POINTER(c_char)
    buttonParams = MOT_ButtonParameters()

    output = CC_SetButtonParamsBlock(serial_number, buttonParams)
    if output != 0:
        raise KinesisException(output)


CC_SetDCPIDParams = lib.CC_SetDCPIDParams
CC_SetDCPIDParams.restype = c_short
CC_SetDCPIDParams.argtypes = [POINTER(c_char), MOT_DC_PIDParameters]


def set_d_c_p_i_d_params(serial_number):
    # Set the PID parameters for DC motors used in an algorithm involving calculus.

    serial_number = POINTER(c_char)
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()

    output = CC_SetDCPIDParams(serial_number, DCproportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


CC_SetDirection = lib.CC_SetDirection
CC_SetDirection.restype = c_void_p
CC_SetDirection.argtypes = [POINTER(c_char), c_bool]


def set_direction(serial_number):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    reverse = c_bool()

    output = CC_SetDirection(serial_number, reverse)
    if output != 0:
        raise KinesisException(output)


CC_SetEncoderCounter = lib.CC_SetEncoderCounter
CC_SetEncoderCounter.restype = c_short
CC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]


def set_encoder_counter(serial_number):
    # Set the Encoder Counter values.

    serial_number = POINTER(c_char)
    count = c_long()

    output = CC_SetEncoderCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


CC_SetHomingParamsBlock = lib.CC_SetHomingParamsBlock
CC_SetHomingParamsBlock.restype = c_short
CC_SetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def set_homing_params_block(serial_number):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = CC_SetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


CC_SetHomingVelocity = lib.CC_SetHomingVelocity
CC_SetHomingVelocity.restype = c_short
CC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]


def set_homing_velocity(serial_number):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    velocity = c_uint()

    output = CC_SetHomingVelocity(serial_number, velocity)
    if output != 0:
        raise KinesisException(output)


CC_SetJogMode = lib.CC_SetJogMode
CC_SetJogMode.restype = c_short
CC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = CC_SetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


CC_SetJogParamsBlock = lib.CC_SetJogParamsBlock
CC_SetJogParamsBlock.restype = c_short
CC_SetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def set_jog_params_block(serial_number):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = CC_SetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


CC_SetJogStepSize = lib.CC_SetJogStepSize
CC_SetJogStepSize.restype = c_short
CC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]


def set_jog_step_size(serial_number):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    stepSize = c_uint()

    output = CC_SetJogStepSize(serial_number, stepSize)
    if output != 0:
        raise KinesisException(output)


CC_SetJogVelParams = lib.CC_SetJogVelParams
CC_SetJogVelParams.restype = c_short
CC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_jog_vel_params(serial_number):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_SetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


CC_SetLEDswitches = lib.CC_SetLEDswitches
CC_SetLEDswitches.restype = c_short
CC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]


def set_l_e_dswitches(serial_number):
    # Set the LED indicator bits on cube.

    serial_number = POINTER(c_char)
    LEDswitches = c_long()

    output = CC_SetLEDswitches(serial_number, LEDswitches)
    if output != 0:
        raise KinesisException(output)


CC_SetLimitSwitchParams = lib.CC_SetLimitSwitchParams
CC_SetLimitSwitchParams.restype = c_short
CC_SetLimitSwitchParams.argtypes = [
    POINTER(c_char),
    MOT_LimitSwitchModes,
    MOT_LimitSwitchModes,
    c_uint,
    c_uint,
    MOT_LimitSwitchSWModes]


def set_limit_switch_params(serial_number):
    # Sets the limit switch parameters.

    serial_number = POINTER(c_char)
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = CC_SetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


CC_SetLimitSwitchParamsBlock = lib.CC_SetLimitSwitchParamsBlock
CC_SetLimitSwitchParamsBlock.restype = c_short
CC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def set_limit_switch_params_block(serial_number):
    # Set the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = CC_SetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


CC_SetLimitsSoftwareApproachPolicy = lib.CC_SetLimitsSoftwareApproachPolicy
CC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
CC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = CC_SetLimitsSoftwareApproachPolicy(serial_number, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


CC_SetMotorParams = lib.CC_SetMotorParams
CC_SetMotorParams.restype = c_short
CC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def set_motor_params(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = CC_SetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


CC_SetMotorParamsExt = lib.CC_SetMotorParamsExt
CC_SetMotorParamsExt.restype = c_short
CC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def set_motor_params_ext(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = CC_SetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


CC_SetMotorTravelLimits = lib.CC_SetMotorTravelLimits
CC_SetMotorTravelLimits.restype = c_short
CC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_travel_limits(serial_number):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = CC_SetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


CC_SetMotorTravelMode = lib.CC_SetMotorTravelMode
CC_SetMotorTravelMode.restype = c_short
CC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]


def set_motor_travel_mode(serial_number):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    travelMode = MOT_TravelModes()

    output = CC_SetMotorTravelMode(serial_number, travelMode)
    if output != 0:
        raise KinesisException(output)


CC_SetMotorVelocityLimits = lib.CC_SetMotorVelocityLimits
CC_SetMotorVelocityLimits.restype = c_short
CC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_velocity_limits(serial_number):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = CC_SetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


CC_SetMoveAbsolutePosition = lib.CC_SetMoveAbsolutePosition
CC_SetMoveAbsolutePosition.restype = c_short
CC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]


def set_move_absolute_position(serial_number):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    position = c_int()

    output = CC_SetMoveAbsolutePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


CC_SetMoveRelativeDistance = lib.CC_SetMoveRelativeDistance
CC_SetMoveRelativeDistance.restype = c_short
CC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]


def set_move_relative_distance(serial_number):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    distance = c_int()

    output = CC_SetMoveRelativeDistance(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


CC_SetPositionCounter = lib.CC_SetPositionCounter
CC_SetPositionCounter.restype = c_short
CC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]


def set_position_counter(serial_number):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    count = c_long()

    output = CC_SetPositionCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


CC_SetPotentiometerParams = lib.CC_SetPotentiometerParams
CC_SetPotentiometerParams.restype = c_short
CC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]


def set_potentiometer_params(serial_number):
    # Sets the potentiometer parameters for the TCube.

    serial_number = POINTER(c_char)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = CC_SetPotentiometerParams(serial_number, index, thresholdDeflection, velocity)
    if output != 0:
        raise KinesisException(output)


CC_SetPotentiometerParamsBlock = lib.CC_SetPotentiometerParamsBlock
CC_SetPotentiometerParamsBlock.restype = c_short
CC_SetPotentiometerParamsBlock.argtypes = [POINTER(c_char), MOT_PotentiometerSteps]


def set_potentiometer_params_block(serial_number):
    # Set the potentiometer parameters.

    serial_number = POINTER(c_char)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = CC_SetPotentiometerParamsBlock(serial_number, potentiometerSteps)
    if output != 0:
        raise KinesisException(output)


CC_SetRotationModes = lib.CC_SetRotationModes
CC_SetRotationModes.restype = c_short
CC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = CC_SetRotationModes(serial_number, mode, direction)
    if output != 0:
        raise KinesisException(output)


CC_SetStageAxisLimits = lib.CC_SetStageAxisLimits
CC_SetStageAxisLimits.restype = c_short
CC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]


def set_stage_axis_limits(serial_number):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    minPosition = c_int()
    maxPosition = c_int()

    output = CC_SetStageAxisLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


CC_SetVelParams = lib.CC_SetVelParams
CC_SetVelParams.restype = c_short
CC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_vel_params(serial_number):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_SetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


CC_SetVelParamsBlock = lib.CC_SetVelParamsBlock
CC_SetVelParamsBlock.restype = c_short
CC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def set_vel_params_block(serial_number):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = CC_SetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


CC_StartPolling = lib.CC_StartPolling
CC_StartPolling.restype = c_bool
CC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = CC_StartPolling(serial_number, milliseconds)

    return output


CC_StopImmediate = lib.CC_StopImmediate
CC_StopImmediate.restype = c_short
CC_StopImmediate.argtypes = [POINTER(c_char)]


def stop_immediate(serial_number):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)

    output = CC_StopImmediate(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_StopPolling = lib.CC_StopPolling
CC_StopPolling.restype = c_void_p
CC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = CC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_StopProfiled = lib.CC_StopProfiled
CC_StopProfiled.restype = c_short
CC_StopProfiled.argtypes = [POINTER(c_char)]


def stop_profiled(serial_number):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)

    output = CC_StopProfiled(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_SuspendMoveMessages = lib.CC_SuspendMoveMessages
CC_SuspendMoveMessages.restype = c_short
CC_SuspendMoveMessages.argtypes = [POINTER(c_char)]


def suspend_move_messages(serial_number):
    # Suspend automatic messages at ends of moves.

    serial_number = POINTER(c_char)

    output = CC_SuspendMoveMessages(serial_number)
    if output != 0:
        raise KinesisException(output)


CC_TimeSinceLastMsgReceived = lib.CC_TimeSinceLastMsgReceived
CC_TimeSinceLastMsgReceived.restype = c_bool
CC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = CC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


CC_WaitForMessage = lib.CC_WaitForMessage
CC_WaitForMessage.restype = c_bool
CC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = CC_WaitForMessage(serial_number, messageType, messageID, messageData)

    return output


TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [c_void_p]


def build_device_list():
    # Build the DeviceList.

    output = TLI_BuildDeviceList()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]


def get_device_info(serial_number):
    # Get the device information from the USB port.

    serial_number = POINTER(c_char)
    serialNumber = POINTER(c_char)
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number, serialNumber, info)
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]


def get_device_list():
    # Get the entire contents of the device list.

    output = TLI_GetDeviceList()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]


def get_device_list_by_type():
    # Get the contents of the device list which match the supplied typeID.

    output = TLI_GetDeviceListByType()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]


def get_device_list_by_type_ext():
    # Get the contents of the device list which match the supplied typeID.

    output = TLI_GetDeviceListByTypeExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]


def get_device_list_by_types():
    # Get the contents of the device list which match the supplied typeIDs.

    output = TLI_GetDeviceListByTypes()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_ulong, c_int, c_int]


def get_device_list_by_types_ext():
    # Get the contents of the device list which match the supplied typeIDs.

    output = TLI_GetDeviceListByTypesExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]


def get_device_list_ext():
    # Get the entire contents of the device list.

    output = TLI_GetDeviceListExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short


def get_device_list_size():
    # Gets the device list size.

    output = TLI_GetDeviceListSize()
    if output != 0:
        raise KinesisException(output)


TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p


def initialize_simulations():
    # Initialize a connection to the Simulation Manager, which must already be running.

    output = TLI_InitializeSimulations()
    if output != 0:
        raise KinesisException(output)
