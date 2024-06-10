from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_float,
    c_int,
    c_int16,
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
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_WheelDirectionSense,
    KMOT_WheelMode,
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
    KMOT_MMIParams,
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_BVC_ScanParams,
    MOT_DC_PIDParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.VoiceCoil.dll")

BVC_CanDeviceLockFrontPanel = lib.BVC_CanDeviceLockFrontPanel
BVC_CanDeviceLockFrontPanel.restype = c_bool
BVC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = BVC_CanDeviceLockFrontPanel(serial_number)

    return output


BVC_CanHome = lib.BVC_CanHome
BVC_CanHome.restype = c_bool
BVC_CanHome.argtypes = [POINTER(c_char)]


def can_home(serial_number):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)

    output = BVC_CanHome(serial_number)

    return output


BVC_CanMoveWithoutHomingFirst = lib.BVC_CanMoveWithoutHomingFirst
BVC_CanMoveWithoutHomingFirst.restype = c_bool
BVC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


def can_move_without_homing_first(serial_number):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)

    output = BVC_CanMoveWithoutHomingFirst(serial_number)

    return output


BVC_CheckConnection = lib.BVC_CheckConnection
BVC_CheckConnection.restype = c_bool
BVC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = BVC_CheckConnection(serial_number)

    return output


BVC_ClearMessageQueue = lib.BVC_ClearMessageQueue
BVC_ClearMessageQueue.restype = c_void_p
BVC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = BVC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_Close = lib.BVC_Close
BVC_Close.restype = c_void_p
BVC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = BVC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_DisableChannel = lib.BVC_DisableChannel
BVC_DisableChannel.restype = c_short
BVC_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel(serial_number):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)

    output = BVC_DisableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_EnableChannel = lib.BVC_EnableChannel
BVC_EnableChannel.restype = c_short
BVC_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel(serial_number):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)

    output = BVC_EnableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_EnableLastMsgTimer = lib.BVC_EnableLastMsgTimer
BVC_EnableLastMsgTimer.restype = c_void_p
BVC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = BVC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


BVC_GetBacklash = lib.BVC_GetBacklash
BVC_GetBacklash.restype = c_long
BVC_GetBacklash.argtypes = [POINTER(c_char)]


def get_backlash(serial_number):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)

    output = BVC_GetBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetDCPIDParams = lib.BVC_GetDCPIDParams
BVC_GetDCPIDParams.restype = c_short
BVC_GetDCPIDParams.argtypes = [POINTER(c_char), MOT_DC_PIDParameters]


def get_d_c_p_i_d_params(serial_number):
    # Get the DC PID parameters for DC motors used in an algorithm involving calculus.

    serial_number = POINTER(c_char)
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()

    output = BVC_GetDCPIDParams(serial_number, DCproportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetDeviceUnitFromRealValue = lib.BVC_GetDeviceUnitFromRealValue
BVC_GetDeviceUnitFromRealValue.restype = c_short
BVC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = BVC_GetDeviceUnitFromRealValue(serial_number, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


BVC_GetDigitalOutputs = lib.BVC_GetDigitalOutputs
BVC_GetDigitalOutputs.restype = c_byte
BVC_GetDigitalOutputs.argtypes = [POINTER(c_char)]


def get_digital_outputs(serial_number):
    # Gets the digital output bits.

    serial_number = POINTER(c_char)

    output = BVC_GetDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetEncoderCounter = lib.BVC_GetEncoderCounter
BVC_GetEncoderCounter.restype = c_long
BVC_GetEncoderCounter.argtypes = [POINTER(c_char)]


def get_encoder_counter(serial_number):
    # Get the Encoder Counter.

    serial_number = POINTER(c_char)

    output = BVC_GetEncoderCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetFrontPanelLocked = lib.BVC_GetFrontPanelLocked
BVC_GetFrontPanelLocked.restype = c_bool
BVC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = BVC_GetFrontPanelLocked(serial_number)

    return output


BVC_GetHardwareInfo = lib.BVC_GetHardwareInfo
BVC_GetHardwareInfo.restype = c_short
BVC_GetHardwareInfo.argtypes = [
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

    output = BVC_GetHardwareInfo(
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


BVC_GetHardwareInfoBlock = lib.BVC_GetHardwareInfoBlock
BVC_GetHardwareInfoBlock.restype = c_short
BVC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = BVC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


BVC_GetHomingParamsBlock = lib.BVC_GetHomingParamsBlock
BVC_GetHomingParamsBlock.restype = c_short
BVC_GetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def get_homing_params_block(serial_number):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = BVC_GetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetHomingVelocity = lib.BVC_GetHomingVelocity
BVC_GetHomingVelocity.restype = c_uint
BVC_GetHomingVelocity.argtypes = [POINTER(c_char)]


def get_homing_velocity(serial_number):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)

    output = BVC_GetHomingVelocity(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetHubBay = lib.BVC_GetHubBay
BVC_GetHubBay.restype = POINTER(c_char)
BVC_GetHubBay.argtypes = [POINTER(c_char)]


def get_hub_bay(serial_number):
    # Gets the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = BVC_GetHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetJogMode = lib.BVC_GetJogMode
BVC_GetJogMode.restype = c_short
BVC_GetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BVC_GetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


BVC_GetJogParamsBlock = lib.BVC_GetJogParamsBlock
BVC_GetJogParamsBlock.restype = c_short
BVC_GetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def get_jog_params_block(serial_number):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = BVC_GetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetJogStepSize = lib.BVC_GetJogStepSize
BVC_GetJogStepSize.restype = c_uint
BVC_GetJogStepSize.argtypes = [POINTER(c_char)]


def get_jog_step_size(serial_number):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)

    output = BVC_GetJogStepSize(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetJogVelParams = lib.BVC_GetJogVelParams
BVC_GetJogVelParams.restype = c_short
BVC_GetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_jog_vel_params(serial_number):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = BVC_GetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BVC_GetLEDswitches = lib.BVC_GetLEDswitches
BVC_GetLEDswitches.restype = c_long
BVC_GetLEDswitches.argtypes = [POINTER(c_char)]


def get_l_e_dswitches(serial_number):
    # Get the LED indicator bits on cube.

    serial_number = POINTER(c_char)

    output = BVC_GetLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetLimitSwitchParams = lib.BVC_GetLimitSwitchParams
BVC_GetLimitSwitchParams.restype = c_short
BVC_GetLimitSwitchParams.argtypes = [
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

    output = BVC_GetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


BVC_GetLimitSwitchParamsBlock = lib.BVC_GetLimitSwitchParamsBlock
BVC_GetLimitSwitchParamsBlock.restype = c_short
BVC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def get_limit_switch_params_block(serial_number):
    # Get the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = BVC_GetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetMMIParams = lib.BVC_GetMMIParams
BVC_GetMMIParams.restype = c_short
BVC_GetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def get_m_m_i_params(serial_number):
    # Get the MMI Parameters for the Voice Coil Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = BVC_GetMMIParams(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity)
    if output != 0:
        raise KinesisException(output)


BVC_GetMMIParamsBlock = lib.BVC_GetMMIParamsBlock
BVC_GetMMIParamsBlock.restype = c_short
BVC_GetMMIParamsBlock.argtypes = [POINTER(c_char), KMOT_MMIParams]


def get_m_m_i_params_block(serial_number):
    # Gets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KMOT_MMIParams()

    output = BVC_GetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetMMIParamsExt = lib.BVC_GetMMIParamsExt
BVC_GetMMIParamsExt.restype = c_short
BVC_GetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16,
    c_int16,
    c_int16]


def get_m_m_i_params_ext(serial_number):
    # Get the MMI Parameters for the Voice Coil Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = BVC_GetMMIParamsExt(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity,
        displayTimeout,
        displayDimIntensity)
    if output != 0:
        raise KinesisException(output)


BVC_GetMotorParams = lib.BVC_GetMotorParams
BVC_GetMotorParams.restype = c_short
BVC_GetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def get_motor_params(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = BVC_GetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BVC_GetMotorParamsExt = lib.BVC_GetMotorParamsExt
BVC_GetMotorParamsExt.restype = c_short
BVC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def get_motor_params_ext(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = BVC_GetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BVC_GetMotorTravelLimits = lib.BVC_GetMotorTravelLimits
BVC_GetMotorTravelLimits.restype = c_short
BVC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_travel_limits(serial_number):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = BVC_GetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BVC_GetMotorTravelMode = lib.BVC_GetMotorTravelMode
BVC_GetMotorTravelMode.restype = MOT_TravelModes
BVC_GetMotorTravelMode.argtypes = [POINTER(c_char)]


def get_motor_travel_mode(serial_number):
    # Get the motor travel mode.

    serial_number = POINTER(c_char)

    output = BVC_GetMotorTravelMode(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetMotorVelocityLimits = lib.BVC_GetMotorVelocityLimits
BVC_GetMotorVelocityLimits.restype = c_short
BVC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_velocity_limits(serial_number):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BVC_GetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


BVC_GetMoveAbsolutePosition = lib.BVC_GetMoveAbsolutePosition
BVC_GetMoveAbsolutePosition.restype = c_int
BVC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def get_move_absolute_position(serial_number):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)

    output = BVC_GetMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetMoveRelativeDistance = lib.BVC_GetMoveRelativeDistance
BVC_GetMoveRelativeDistance.restype = c_int
BVC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


def get_move_relative_distance(serial_number):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)

    output = BVC_GetMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetNextMessage = lib.BVC_GetNextMessage
BVC_GetNextMessage.restype = c_bool
BVC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BVC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


BVC_GetNumberPositions = lib.BVC_GetNumberPositions
BVC_GetNumberPositions.restype = c_int
BVC_GetNumberPositions.argtypes = [POINTER(c_char)]


def get_number_positions(serial_number):
    # Get number of positions.

    serial_number = POINTER(c_char)

    output = BVC_GetNumberPositions(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetPosition = lib.BVC_GetPosition
BVC_GetPosition.restype = c_int
BVC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)

    output = BVC_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetPositionCounter = lib.BVC_GetPositionCounter
BVC_GetPositionCounter.restype = c_long
BVC_GetPositionCounter.argtypes = [POINTER(c_char)]


def get_position_counter(serial_number):
    # Get the Position Counter.

    serial_number = POINTER(c_char)

    output = BVC_GetPositionCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetRealValueFromDeviceUnit = lib.BVC_GetRealValueFromDeviceUnit
BVC_GetRealValueFromDeviceUnit.restype = c_short
BVC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = BVC_GetRealValueFromDeviceUnit(serial_number, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


BVC_GetScanParams = lib.BVC_GetScanParams
BVC_GetScanParams.restype = c_short
BVC_GetScanParams.argtypes = [POINTER(c_char), MOT_BVC_ScanParams]


def get_scan_params(serial_number):
    # Gets the BVC Scan parameters.

    serial_number = POINTER(c_char)
    scanParameters = MOT_BVC_ScanParams()

    output = BVC_GetScanParams(serial_number, scanParameters)
    if output != 0:
        raise KinesisException(output)


BVC_GetSoftLimitMode = lib.BVC_GetSoftLimitMode
BVC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BVC_GetSoftLimitMode.argtypes = [POINTER(c_char)]


def get_soft_limit_mode(serial_number):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)

    output = BVC_GetSoftLimitMode(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetSoftwareVersion = lib.BVC_GetSoftwareVersion
BVC_GetSoftwareVersion.restype = c_ulong
BVC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = BVC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetStageAxisMaxPos = lib.BVC_GetStageAxisMaxPos
BVC_GetStageAxisMaxPos.restype = c_int
BVC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


def get_stage_axis_max_pos(serial_number):
    # Gets the DC Motor maximum stage position.

    serial_number = POINTER(c_char)

    output = BVC_GetStageAxisMaxPos(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetStageAxisMinPos = lib.BVC_GetStageAxisMinPos
BVC_GetStageAxisMinPos.restype = c_int
BVC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


def get_stage_axis_min_pos(serial_number):
    # Gets the DC Motor minimum stage position.

    serial_number = POINTER(c_char)

    output = BVC_GetStageAxisMinPos(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetStatusBits = lib.BVC_GetStatusBits
BVC_GetStatusBits.restype = c_ulong
BVC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = BVC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_GetTriggerConfigParams = lib.BVC_GetTriggerConfigParams
BVC_GetTriggerConfigParams.restype = c_short
BVC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]


def get_trigger_config_params(serial_number):
    # Get the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BVC_GetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


BVC_GetTriggerConfigParamsBlock = lib.BVC_GetTriggerConfigParamsBlock
BVC_GetTriggerConfigParamsBlock.restype = c_short
BVC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]


def get_trigger_config_params_block(serial_number):
    # Gets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KMOT_TriggerConfig()

    output = BVC_GetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetTriggerParamsParams = lib.BVC_GetTriggerParamsParams
BVC_GetTriggerParamsParams.restype = c_short
BVC_GetTriggerParamsParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]


def get_trigger_params_params(serial_number):
    # Get the Trigger Parameters Parameters.

    serial_number = POINTER(c_char)
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BVC_GetTriggerParamsParams(
        serial_number,
        triggerStartPositionFwd,
        triggerIntervalFwd,
        triggerPulseCountFwd,
        triggerStartPositionRev,
        triggerIntervalRev,
        triggerPulseCountRev,
        triggerPulseWidth,
        cycleCount)
    if output != 0:
        raise KinesisException(output)


BVC_GetTriggerParamsParamsBlock = lib.BVC_GetTriggerParamsParamsBlock
BVC_GetTriggerParamsParamsBlock.restype = c_short
BVC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]


def get_trigger_params_params_block(serial_number):
    # Gets the trigger parameters block.

    serial_number = POINTER(c_char)
    triggerParamsParams = KMOT_TriggerParams()

    output = BVC_GetTriggerParamsParamsBlock(serial_number, triggerParamsParams)
    if output != 0:
        raise KinesisException(output)


BVC_GetVelParams = lib.BVC_GetVelParams
BVC_GetVelParams.restype = c_short
BVC_GetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_vel_params(serial_number):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = BVC_GetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BVC_GetVelParamsBlock = lib.BVC_GetVelParamsBlock
BVC_GetVelParamsBlock.restype = c_short
BVC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def get_vel_params_block(serial_number):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = BVC_GetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


BVC_HasLastMsgTimerOverrun = lib.BVC_HasLastMsgTimerOverrun
BVC_HasLastMsgTimerOverrun.restype = c_bool
BVC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by BVC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = BVC_HasLastMsgTimerOverrun(serial_number)

    return output


BVC_Home = lib.BVC_Home
BVC_Home.restype = c_short
BVC_Home.argtypes = [POINTER(c_char)]


def home(serial_number):
    # Home the device.

    serial_number = POINTER(c_char)

    output = BVC_Home(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_Identify = lib.BVC_Identify
BVC_Identify.restype = c_void_p
BVC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = BVC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_IsScanning = lib.BVC_IsScanning
BVC_IsScanning.restype = c_bool
BVC_IsScanning.argtypes = [POINTER(c_char)]


def is_scanning(serial_number):
    # Gets the Scanning state.

    serial_number = POINTER(c_char)

    output = BVC_IsScanning(serial_number)

    return output


BVC_IsScanningEnabled = lib.BVC_IsScanningEnabled
BVC_IsScanningEnabled.restype = c_bool
BVC_IsScanningEnabled.argtypes = [POINTER(c_char)]


def is_scanning_enabled(serial_number):
    # get whether BVC is scanning.

    serial_number = POINTER(c_char)

    output = BVC_IsScanningEnabled(serial_number)

    return output


BVC_LoadNamedSettings = lib.BVC_LoadNamedSettings
BVC_LoadNamedSettings.restype = c_bool
BVC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = BVC_LoadNamedSettings(serial_number, settingsName)

    return output


BVC_LoadSettings = lib.BVC_LoadSettings
BVC_LoadSettings.restype = c_bool
BVC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = BVC_LoadSettings(serial_number)

    return output


BVC_MessageQueueSize = lib.BVC_MessageQueueSize
BVC_MessageQueueSize.restype = c_int
BVC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = BVC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_MoveAbsolute = lib.BVC_MoveAbsolute
BVC_MoveAbsolute.restype = c_short
BVC_MoveAbsolute.argtypes = [POINTER(c_char)]


def move_absolute(serial_number):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)

    output = BVC_MoveAbsolute(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_MoveAtVelocity = lib.BVC_MoveAtVelocity
BVC_MoveAtVelocity.restype = c_short
BVC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_at_velocity(serial_number):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    direction = MOT_TravelDirection()

    output = BVC_MoveAtVelocity(serial_number, direction)
    if output != 0:
        raise KinesisException(output)


BVC_MoveJog = lib.BVC_MoveJog
BVC_MoveJog.restype = c_short
BVC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_jog(serial_number):
    # Perform a jog.

    serial_number = POINTER(c_char)
    jogDirection = MOT_TravelDirection()

    output = BVC_MoveJog(serial_number, jogDirection)
    if output != 0:
        raise KinesisException(output)


BVC_MoveRelative = lib.BVC_MoveRelative
BVC_MoveRelative.restype = c_short
BVC_MoveRelative.argtypes = [POINTER(c_char), c_int]


def move_relative(serial_number):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    displacement = c_int()

    output = BVC_MoveRelative(serial_number, displacement)
    if output != 0:
        raise KinesisException(output)


BVC_MoveRelativeDistance = lib.BVC_MoveRelativeDistance
BVC_MoveRelativeDistance.restype = c_short
BVC_MoveRelativeDistance.argtypes = [POINTER(c_char)]


def move_relative_distance(serial_number):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)

    output = BVC_MoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_MoveToPosition = lib.BVC_MoveToPosition
BVC_MoveToPosition.restype = c_short
BVC_MoveToPosition.argtypes = [POINTER(c_char), c_int]


def move_to_position(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    index = c_int()

    output = BVC_MoveToPosition(serial_number, index)
    if output != 0:
        raise KinesisException(output)


BVC_NeedsHoming = lib.BVC_NeedsHoming
BVC_NeedsHoming.restype = c_bool
BVC_NeedsHoming.argtypes = [POINTER(c_char)]


def needs_homing(serial_number):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)

    output = BVC_NeedsHoming(serial_number)

    return output


BVC_Open = lib.BVC_Open
BVC_Open.restype = c_short
BVC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = BVC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_PersistSettings = lib.BVC_PersistSettings
BVC_PersistSettings.restype = c_bool
BVC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = BVC_PersistSettings(serial_number)

    return output


BVC_PollingDuration = lib.BVC_PollingDuration
BVC_PollingDuration.restype = c_long
BVC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = BVC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RegisterMessageCallback = lib.BVC_RegisterMessageCallback
BVC_RegisterMessageCallback.restype = c_void_p
BVC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = BVC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


BVC_RequestBacklash = lib.BVC_RequestBacklash
BVC_RequestBacklash.restype = c_short
BVC_RequestBacklash.argtypes = [POINTER(c_char)]


def request_backlash(serial_number):
    # Requests the backlash.

    serial_number = POINTER(c_char)

    output = BVC_RequestBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestDCPIDParams = lib.BVC_RequestDCPIDParams
BVC_RequestDCPIDParams.restype = c_short
BVC_RequestDCPIDParams.argtypes = [POINTER(c_char)]


def request_d_c_p_i_d_params(serial_number):
    # Request the PID parameters for DC motors used in an algorithm involving calculus.

    serial_number = POINTER(c_char)

    output = BVC_RequestDCPIDParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestDigitalOutputs = lib.BVC_RequestDigitalOutputs
BVC_RequestDigitalOutputs.restype = c_short
BVC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]


def request_digital_outputs(serial_number):
    # Requests the digital output bits.

    serial_number = POINTER(c_char)

    output = BVC_RequestDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestEncoderCounter = lib.BVC_RequestEncoderCounter
BVC_RequestEncoderCounter.restype = c_short
BVC_RequestEncoderCounter.argtypes = [POINTER(c_char)]


def request_encoder_counter(serial_number):
    # Requests the encoder counter.

    serial_number = POINTER(c_char)

    output = BVC_RequestEncoderCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestFrontPanelLocked = lib.BVC_RequestFrontPanelLocked
BVC_RequestFrontPanelLocked.restype = c_short
BVC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = BVC_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestHomingParams = lib.BVC_RequestHomingParams
BVC_RequestHomingParams.restype = c_short
BVC_RequestHomingParams.argtypes = [POINTER(c_char)]


def request_homing_params(serial_number):
    # Requests the homing parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestHomingParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestJogParams = lib.BVC_RequestJogParams
BVC_RequestJogParams.restype = c_short
BVC_RequestJogParams.argtypes = [POINTER(c_char)]


def request_jog_params(serial_number):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestJogParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestLEDswitches = lib.BVC_RequestLEDswitches
BVC_RequestLEDswitches.restype = c_short
BVC_RequestLEDswitches.argtypes = [POINTER(c_char)]


def request_l_e_dswitches(serial_number):
    # Request the LED indicator bits on cube.

    serial_number = POINTER(c_char)

    output = BVC_RequestLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestLimitSwitchParams = lib.BVC_RequestLimitSwitchParams
BVC_RequestLimitSwitchParams.restype = c_short
BVC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]


def request_limit_switch_params(serial_number):
    # Requests the limit switch parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestLimitSwitchParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestMMIparams = lib.BVC_RequestMMIparams
BVC_RequestMMIparams.restype = c_short
BVC_RequestMMIparams.argtypes = [POINTER(c_char)]


def request_m_m_iparams(serial_number):
    # Requests the MMI Parameters for the Voice Coil Display Interface.

    serial_number = POINTER(c_char)

    output = BVC_RequestMMIparams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestMoveAbsolutePosition = lib.BVC_RequestMoveAbsolutePosition
BVC_RequestMoveAbsolutePosition.restype = c_short
BVC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def request_move_absolute_position(serial_number):
    # Requests the position of next absolute move.

    serial_number = POINTER(c_char)

    output = BVC_RequestMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestMoveRelativeDistance = lib.BVC_RequestMoveRelativeDistance
BVC_RequestMoveRelativeDistance.restype = c_short
BVC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


def request_move_relative_distance(serial_number):
    # Requests the relative move distance.

    serial_number = POINTER(c_char)

    output = BVC_RequestMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestPosTriggerParams = lib.BVC_RequestPosTriggerParams
BVC_RequestPosTriggerParams.restype = c_short
BVC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]


def request_pos_trigger_params(serial_number):
    # Requests the position trigger parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestPosTriggerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestPosition = lib.BVC_RequestPosition
BVC_RequestPosition.restype = c_short
BVC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current position.

    serial_number = POINTER(c_char)

    output = BVC_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestScanParams = lib.BVC_RequestScanParams
BVC_RequestScanParams.restype = c_short
BVC_RequestScanParams.argtypes = [POINTER(c_char)]


def request_scan_params(serial_number):
    # Requests the BVC Scan parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestScanParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestSettings = lib.BVC_RequestSettings
BVC_RequestSettings.restype = c_short
BVC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = BVC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestStatusBits = lib.BVC_RequestStatusBits
BVC_RequestStatusBits.restype = c_short
BVC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)

    output = BVC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestTriggerConfigParams = lib.BVC_RequestTriggerConfigParams
BVC_RequestTriggerConfigParams.restype = c_short
BVC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    # Requests the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestTriggerConfigParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_RequestVelParams = lib.BVC_RequestVelParams
BVC_RequestVelParams.restype = c_short
BVC_RequestVelParams.argtypes = [POINTER(c_char)]


def request_vel_params(serial_number):
    # Requests the velocity parameters.

    serial_number = POINTER(c_char)

    output = BVC_RequestVelParams(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_ResetRotationModes = lib.BVC_ResetRotationModes
BVC_ResetRotationModes.restype = c_short
BVC_ResetRotationModes.argtypes = [POINTER(c_char)]


def reset_rotation_modes(serial_number):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)

    output = BVC_ResetRotationModes(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_ResetStageToDefaults = lib.BVC_ResetStageToDefaults
BVC_ResetStageToDefaults.restype = c_short
BVC_ResetStageToDefaults.argtypes = [POINTER(c_char)]


def reset_stage_to_defaults(serial_number):
    # Reset the stage settings to defaults.

    serial_number = POINTER(c_char)

    output = BVC_ResetStageToDefaults(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_ResumeMoveMessages = lib.BVC_ResumeMoveMessages
BVC_ResumeMoveMessages.restype = c_short
BVC_ResumeMoveMessages.argtypes = [POINTER(c_char)]


def resume_move_messages(serial_number):
    # Resume suspended move messages.

    serial_number = POINTER(c_char)

    output = BVC_ResumeMoveMessages(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_SetBacklash = lib.BVC_SetBacklash
BVC_SetBacklash.restype = c_short
BVC_SetBacklash.argtypes = [POINTER(c_char), c_long]


def set_backlash(serial_number):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    distance = c_long()

    output = BVC_SetBacklash(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


BVC_SetDCPIDParams = lib.BVC_SetDCPIDParams
BVC_SetDCPIDParams.restype = c_short
BVC_SetDCPIDParams.argtypes = [POINTER(c_char), MOT_DC_PIDParameters]


def set_d_c_p_i_d_params(serial_number):
    # Set the PID parameters for DC motors used in an algorithm involving calculus.

    serial_number = POINTER(c_char)
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()

    output = BVC_SetDCPIDParams(serial_number, DCproportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetDigitalOutputs = lib.BVC_SetDigitalOutputs
BVC_SetDigitalOutputs.restype = c_short
BVC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]


def set_digital_outputs(serial_number):
    # Sets the digital output bits.

    serial_number = POINTER(c_char)
    outputsBits = c_byte()

    output = BVC_SetDigitalOutputs(serial_number, outputsBits)
    if output != 0:
        raise KinesisException(output)


BVC_SetDirection = lib.BVC_SetDirection
BVC_SetDirection.restype = c_void_p
BVC_SetDirection.argtypes = [POINTER(c_char), c_bool]


def set_direction(serial_number):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    reverse = c_bool()

    output = BVC_SetDirection(serial_number, reverse)
    if output != 0:
        raise KinesisException(output)


BVC_SetEncoderCounter = lib.BVC_SetEncoderCounter
BVC_SetEncoderCounter.restype = c_short
BVC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]


def set_encoder_counter(serial_number):
    # Set the Encoder Counter values.

    serial_number = POINTER(c_char)
    count = c_long()

    output = BVC_SetEncoderCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


BVC_SetFrontPanelLock = lib.BVC_SetFrontPanelLock
BVC_SetFrontPanelLock.restype = c_short
BVC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = BVC_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


BVC_SetHomingParamsBlock = lib.BVC_SetHomingParamsBlock
BVC_SetHomingParamsBlock.restype = c_short
BVC_SetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def set_homing_params_block(serial_number):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = BVC_SetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetHomingVelocity = lib.BVC_SetHomingVelocity
BVC_SetHomingVelocity.restype = c_short
BVC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]


def set_homing_velocity(serial_number):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    velocity = c_uint()

    output = BVC_SetHomingVelocity(serial_number, velocity)
    if output != 0:
        raise KinesisException(output)


BVC_SetJogMode = lib.BVC_SetJogMode
BVC_SetJogMode.restype = c_short
BVC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BVC_SetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


BVC_SetJogParamsBlock = lib.BVC_SetJogParamsBlock
BVC_SetJogParamsBlock.restype = c_short
BVC_SetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def set_jog_params_block(serial_number):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = BVC_SetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetJogStepSize = lib.BVC_SetJogStepSize
BVC_SetJogStepSize.restype = c_short
BVC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]


def set_jog_step_size(serial_number):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    stepSize = c_uint()

    output = BVC_SetJogStepSize(serial_number, stepSize)
    if output != 0:
        raise KinesisException(output)


BVC_SetJogVelParams = lib.BVC_SetJogVelParams
BVC_SetJogVelParams.restype = c_short
BVC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_jog_vel_params(serial_number):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = BVC_SetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BVC_SetLEDswitches = lib.BVC_SetLEDswitches
BVC_SetLEDswitches.restype = c_short
BVC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]


def set_l_e_dswitches(serial_number):
    # Set the LED indicator bits on cube.

    serial_number = POINTER(c_char)
    LEDswitches = c_long()

    output = BVC_SetLEDswitches(serial_number, LEDswitches)
    if output != 0:
        raise KinesisException(output)


BVC_SetLimitSwitchParams = lib.BVC_SetLimitSwitchParams
BVC_SetLimitSwitchParams.restype = c_short
BVC_SetLimitSwitchParams.argtypes = [
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

    output = BVC_SetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


BVC_SetLimitSwitchParamsBlock = lib.BVC_SetLimitSwitchParamsBlock
BVC_SetLimitSwitchParamsBlock.restype = c_short
BVC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def set_limit_switch_params_block(serial_number):
    # Set the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = BVC_SetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetLimitsSoftwareApproachPolicy = lib.BVC_SetLimitsSoftwareApproachPolicy
BVC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
BVC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = BVC_SetLimitsSoftwareApproachPolicy(serial_number, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


BVC_SetMMIParams = lib.BVC_SetMMIParams
BVC_SetMMIParams.restype = c_short
BVC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def set_m_m_i_params(serial_number):
    # Set the MMI Parameters for the Voice Coil Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = BVC_SetMMIParams(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity)
    if output != 0:
        raise KinesisException(output)


BVC_SetMMIParamsBlock = lib.BVC_SetMMIParamsBlock
BVC_SetMMIParamsBlock.restype = c_short
BVC_SetMMIParamsBlock.argtypes = [POINTER(c_char), KMOT_MMIParams]


def set_m_m_i_params_block(serial_number):
    # Sets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KMOT_MMIParams()

    output = BVC_SetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetMMIParamsExt = lib.BVC_SetMMIParamsExt
BVC_SetMMIParamsExt.restype = c_short
BVC_SetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16,
    c_int16,
    c_int16]


def set_m_m_i_params_ext(serial_number):
    # Set the MMI Parameters for the Voice Coil Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = BVC_SetMMIParamsExt(
        serial_number,
        wheelMode,
        wheelMaxVelocity,
        wheelAcceleration,
        directionSense,
        presetPosition1,
        presetPosition2,
        displayIntensity,
        displayTimeout,
        displayDimIntensity)
    if output != 0:
        raise KinesisException(output)


BVC_SetMotorParams = lib.BVC_SetMotorParams
BVC_SetMotorParams.restype = c_short
BVC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def set_motor_params(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = BVC_SetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BVC_SetMotorParamsExt = lib.BVC_SetMotorParamsExt
BVC_SetMotorParamsExt.restype = c_short
BVC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def set_motor_params_ext(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = BVC_SetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BVC_SetMotorTravelLimits = lib.BVC_SetMotorTravelLimits
BVC_SetMotorTravelLimits.restype = c_short
BVC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_travel_limits(serial_number):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = BVC_SetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BVC_SetMotorTravelMode = lib.BVC_SetMotorTravelMode
BVC_SetMotorTravelMode.restype = c_short
BVC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]


def set_motor_travel_mode(serial_number):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    travelMode = MOT_TravelModes()

    output = BVC_SetMotorTravelMode(serial_number, travelMode)
    if output != 0:
        raise KinesisException(output)


BVC_SetMotorVelocityLimits = lib.BVC_SetMotorVelocityLimits
BVC_SetMotorVelocityLimits.restype = c_short
BVC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_velocity_limits(serial_number):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BVC_SetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


BVC_SetMoveAbsolutePosition = lib.BVC_SetMoveAbsolutePosition
BVC_SetMoveAbsolutePosition.restype = c_short
BVC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]


def set_move_absolute_position(serial_number):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    position = c_int()

    output = BVC_SetMoveAbsolutePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


BVC_SetMoveRelativeDistance = lib.BVC_SetMoveRelativeDistance
BVC_SetMoveRelativeDistance.restype = c_short
BVC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]


def set_move_relative_distance(serial_number):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    distance = c_int()

    output = BVC_SetMoveRelativeDistance(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


BVC_SetPositionCounter = lib.BVC_SetPositionCounter
BVC_SetPositionCounter.restype = c_short
BVC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]


def set_position_counter(serial_number):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    count = c_long()

    output = BVC_SetPositionCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


BVC_SetRotationModes = lib.BVC_SetRotationModes
BVC_SetRotationModes.restype = c_short
BVC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = BVC_SetRotationModes(serial_number, mode, direction)
    if output != 0:
        raise KinesisException(output)


BVC_SetScanParams = lib.BVC_SetScanParams
BVC_SetScanParams.restype = c_short
BVC_SetScanParams.argtypes = [POINTER(c_char), MOT_BVC_ScanParams]


def set_scan_params(serial_number):
    # Set the BVC Scan parameters.

    serial_number = POINTER(c_char)
    scanParameters = MOT_BVC_ScanParams()

    output = BVC_SetScanParams(serial_number, scanParameters)
    if output != 0:
        raise KinesisException(output)


BVC_SetStageAxisLimits = lib.BVC_SetStageAxisLimits
BVC_SetStageAxisLimits.restype = c_short
BVC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]


def set_stage_axis_limits(serial_number):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    minPosition = c_int()
    maxPosition = c_int()

    output = BVC_SetStageAxisLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BVC_SetTriggerConfigParams = lib.BVC_SetTriggerConfigParams
BVC_SetTriggerConfigParams.restype = c_short
BVC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]


def set_trigger_config_params(serial_number):
    # Set the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BVC_SetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


BVC_SetTriggerConfigParamsBlock = lib.BVC_SetTriggerConfigParamsBlock
BVC_SetTriggerConfigParamsBlock.restype = c_short
BVC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]


def set_trigger_config_params_block(serial_number):
    # Sets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KMOT_TriggerConfig()

    output = BVC_SetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetTriggerParamsParams = lib.BVC_SetTriggerParamsParams
BVC_SetTriggerParamsParams.restype = c_short
BVC_SetTriggerParamsParams.argtypes = [
    POINTER(c_char),
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]


def set_trigger_params_params(serial_number):
    # Set the Trigger Parameters Parameters.

    serial_number = POINTER(c_char)
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BVC_SetTriggerParamsParams(
        serial_number,
        triggerStartPositionFwd,
        triggerIntervalFwd,
        triggerPulseCountFwd,
        triggerStartPositionRev,
        triggerIntervalRev,
        triggerPulseCountRev,
        triggerPulseWidth,
        cycleCount)
    if output != 0:
        raise KinesisException(output)


BVC_SetTriggerParamsParamsBlock = lib.BVC_SetTriggerParamsParamsBlock
BVC_SetTriggerParamsParamsBlock.restype = c_short
BVC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]


def set_trigger_params_params_block(serial_number):
    # Sets the trigger parameters block.

    serial_number = POINTER(c_char)
    triggerParamsParams = KMOT_TriggerParams()

    output = BVC_SetTriggerParamsParamsBlock(serial_number, triggerParamsParams)
    if output != 0:
        raise KinesisException(output)


BVC_SetVelParams = lib.BVC_SetVelParams
BVC_SetVelParams.restype = c_short
BVC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_vel_params(serial_number):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = BVC_SetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BVC_SetVelParamsBlock = lib.BVC_SetVelParamsBlock
BVC_SetVelParamsBlock.restype = c_short
BVC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def set_vel_params_block(serial_number):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = BVC_SetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


BVC_StartPolling = lib.BVC_StartPolling
BVC_StartPolling.restype = c_bool
BVC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = BVC_StartPolling(serial_number, milliseconds)

    return output


BVC_StartScanning = lib.BVC_StartScanning
BVC_StartScanning.restype = c_short
BVC_StartScanning.argtypes = [POINTER(c_char)]


def start_scanning(serial_number):
    # Starts a scanning.

    serial_number = POINTER(c_char)

    output = BVC_StartScanning(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_StopImmediate = lib.BVC_StopImmediate
BVC_StopImmediate.restype = c_short
BVC_StopImmediate.argtypes = [POINTER(c_char)]


def stop_immediate(serial_number):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)

    output = BVC_StopImmediate(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_StopPolling = lib.BVC_StopPolling
BVC_StopPolling.restype = c_void_p
BVC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = BVC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_StopProfiled = lib.BVC_StopProfiled
BVC_StopProfiled.restype = c_short
BVC_StopProfiled.argtypes = [POINTER(c_char)]


def stop_profiled(serial_number):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)

    output = BVC_StopProfiled(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_StopScanning = lib.BVC_StopScanning
BVC_StopScanning.restype = c_short
BVC_StopScanning.argtypes = [POINTER(c_char)]


def stop_scanning(serial_number):
    # Stops a scanning.

    serial_number = POINTER(c_char)

    output = BVC_StopScanning(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_SuspendMoveMessages = lib.BVC_SuspendMoveMessages
BVC_SuspendMoveMessages.restype = c_short
BVC_SuspendMoveMessages.argtypes = [POINTER(c_char)]


def suspend_move_messages(serial_number):
    # Suspend automatic messages at ends of moves.

    serial_number = POINTER(c_char)

    output = BVC_SuspendMoveMessages(serial_number)
    if output != 0:
        raise KinesisException(output)


BVC_TimeSinceLastMsgReceived = lib.BVC_TimeSinceLastMsgReceived
BVC_TimeSinceLastMsgReceived.restype = c_bool
BVC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = BVC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


BVC_WaitForMessage = lib.BVC_WaitForMessage
BVC_WaitForMessage.restype = c_bool
BVC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BVC_WaitForMessage(serial_number, messageType, messageID, messageData)

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
