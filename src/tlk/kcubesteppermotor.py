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
    KST_Stages,
    MOT_JogModes,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchSWModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes,
    TST_Stages)
from .definitions.structures import (
    KMOT_MMIParams,
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PIDLoopEncoderParams,
    MOT_PowerParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.StepperMotor.DLL")

SCC_CanDeviceLockFrontPanel = lib.SCC_CanDeviceLockFrontPanel
SCC_CanDeviceLockFrontPanel.restype = c_bool
SCC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = SCC_CanDeviceLockFrontPanel(serial_number)

    return output


SCC_CanHome = lib.SCC_CanHome
SCC_CanHome.restype = c_bool
SCC_CanHome.argtypes = [POINTER(c_char)]


def can_home(serial_number):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)

    output = SCC_CanHome(serial_number)

    return output


SCC_CanMoveWithoutHomingFirst = lib.SCC_CanMoveWithoutHomingFirst
SCC_CanMoveWithoutHomingFirst.restype = c_bool
SCC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


def can_move_without_homing_first(serial_number):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)

    output = SCC_CanMoveWithoutHomingFirst(serial_number)

    return output


SCC_CheckConnection = lib.SCC_CheckConnection
SCC_CheckConnection.restype = c_bool
SCC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = SCC_CheckConnection(serial_number)

    return output


SCC_ClearMessageQueue = lib.SCC_ClearMessageQueue
SCC_ClearMessageQueue.restype = c_void_p
SCC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = SCC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_Close = lib.SCC_Close
SCC_Close.restype = c_void_p
SCC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = SCC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_DisableChannel = lib.SCC_DisableChannel
SCC_DisableChannel.restype = c_short
SCC_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel(serial_number):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)

    output = SCC_DisableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_EnableChannel = lib.SCC_EnableChannel
SCC_EnableChannel.restype = c_short
SCC_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel(serial_number):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)

    output = SCC_EnableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_EnableLastMsgTimer = lib.SCC_EnableLastMsgTimer
SCC_EnableLastMsgTimer.restype = c_void_p
SCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SCC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


SCC_GetBacklash = lib.SCC_GetBacklash
SCC_GetBacklash.restype = c_long
SCC_GetBacklash.argtypes = [POINTER(c_char)]


def get_backlash(serial_number):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)

    output = SCC_GetBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetBowIndex = lib.SCC_GetBowIndex
SCC_GetBowIndex.restype = c_short
SCC_GetBowIndex.argtypes = [POINTER(c_char)]


def get_bow_index(serial_number):
    # Gets the stepper motor bow index.

    serial_number = POINTER(c_char)

    output = SCC_GetBowIndex(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetCalibrationFile = lib.SCC_GetCalibrationFile
SCC_GetCalibrationFile.restype = c_bool
SCC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short]


def get_calibration_file(serial_number):
    # Get calibration file for this motor.

    serial_number = POINTER(c_char)
    filename = POINTER(c_char)
    sizeOfBuffer = c_short()

    output = SCC_GetCalibrationFile(serial_number, filename, sizeOfBuffer)

    return output


SCC_GetDeviceUnitFromRealValue = lib.SCC_GetDeviceUnitFromRealValue
SCC_GetDeviceUnitFromRealValue.restype = c_short
SCC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = SCC_GetDeviceUnitFromRealValue(serial_number, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


SCC_GetDigitalOutputs = lib.SCC_GetDigitalOutputs
SCC_GetDigitalOutputs.restype = c_byte
SCC_GetDigitalOutputs.argtypes = [POINTER(c_char)]


def get_digital_outputs(serial_number):
    # Gets the digital output bits.

    serial_number = POINTER(c_char)

    output = SCC_GetDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetEncoderCounter = lib.SCC_GetEncoderCounter
SCC_GetEncoderCounter.restype = c_long
SCC_GetEncoderCounter.argtypes = [POINTER(c_char)]


def get_encoder_counter(serial_number):
    # Get the Encoder Counter.

    serial_number = POINTER(c_char)

    output = SCC_GetEncoderCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetFrontPanelLocked = lib.SCC_GetFrontPanelLocked
SCC_GetFrontPanelLocked.restype = c_bool
SCC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = SCC_GetFrontPanelLocked(serial_number)

    return output


SCC_GetHardwareInfo = lib.SCC_GetHardwareInfo
SCC_GetHardwareInfo.restype = c_short
SCC_GetHardwareInfo.argtypes = [
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

    output = SCC_GetHardwareInfo(
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


SCC_GetHardwareInfoBlock = lib.SCC_GetHardwareInfoBlock
SCC_GetHardwareInfoBlock.restype = c_short
SCC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = SCC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


SCC_GetHomingParamsBlock = lib.SCC_GetHomingParamsBlock
SCC_GetHomingParamsBlock.restype = c_short
SCC_GetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def get_homing_params_block(serial_number):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = SCC_GetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetHomingVelocity = lib.SCC_GetHomingVelocity
SCC_GetHomingVelocity.restype = c_uint
SCC_GetHomingVelocity.argtypes = [POINTER(c_char)]


def get_homing_velocity(serial_number):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)

    output = SCC_GetHomingVelocity(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetHubBay = lib.SCC_GetHubBay
SCC_GetHubBay.restype = POINTER(c_char)
SCC_GetHubBay.argtypes = [POINTER(c_char)]


def get_hub_bay(serial_number):
    # Gets the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = SCC_GetHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetJogMode = lib.SCC_GetJogMode
SCC_GetJogMode.restype = c_short
SCC_GetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SCC_GetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


SCC_GetJogParamsBlock = lib.SCC_GetJogParamsBlock
SCC_GetJogParamsBlock.restype = c_short
SCC_GetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def get_jog_params_block(serial_number):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = SCC_GetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetJogStepSize = lib.SCC_GetJogStepSize
SCC_GetJogStepSize.restype = c_uint
SCC_GetJogStepSize.argtypes = [POINTER(c_char)]


def get_jog_step_size(serial_number):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)

    output = SCC_GetJogStepSize(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetJogVelParams = lib.SCC_GetJogVelParams
SCC_GetJogVelParams.restype = c_short
SCC_GetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_jog_vel_params(serial_number):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_GetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SCC_GetLimitSwitchParams = lib.SCC_GetLimitSwitchParams
SCC_GetLimitSwitchParams.restype = c_short
SCC_GetLimitSwitchParams.argtypes = [
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

    output = SCC_GetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


SCC_GetLimitSwitchParamsBlock = lib.SCC_GetLimitSwitchParamsBlock
SCC_GetLimitSwitchParamsBlock.restype = c_short
SCC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def get_limit_switch_params_block(serial_number):
    # Get the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SCC_GetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetMMIParams = lib.SCC_GetMMIParams
SCC_GetMMIParams.restype = c_short
SCC_GetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def get_m_m_i_params(serial_number):
    # Get the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = SCC_GetMMIParams(
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


SCC_GetMMIParamsBlock = lib.SCC_GetMMIParamsBlock
SCC_GetMMIParamsBlock.restype = c_short
SCC_GetMMIParamsBlock.argtypes = [POINTER(c_char), KMOT_MMIParams]


def get_m_m_i_params_block(serial_number):
    # Gets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KMOT_MMIParams()

    output = SCC_GetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetMMIParamsExt = lib.SCC_GetMMIParamsExt
SCC_GetMMIParamsExt.restype = c_short
SCC_GetMMIParamsExt.argtypes = [
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
    # Get the MMI Parameters for the KCube Display Interface.

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

    output = SCC_GetMMIParamsExt(
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


SCC_GetMotorParams = lib.SCC_GetMotorParams
SCC_GetMotorParams.restype = c_short
SCC_GetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def get_motor_params(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SCC_GetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SCC_GetMotorParamsExt = lib.SCC_GetMotorParamsExt
SCC_GetMotorParamsExt.restype = c_short
SCC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def get_motor_params_ext(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SCC_GetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SCC_GetMotorTravelLimits = lib.SCC_GetMotorTravelLimits
SCC_GetMotorTravelLimits.restype = c_short
SCC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_travel_limits(serial_number):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = SCC_GetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


SCC_GetMotorTravelMode = lib.SCC_GetMotorTravelMode
SCC_GetMotorTravelMode.restype = MOT_TravelModes
SCC_GetMotorTravelMode.argtypes = [POINTER(c_char)]


def get_motor_travel_mode(serial_number):
    # Get the motor travel mode.

    serial_number = POINTER(c_char)

    output = SCC_GetMotorTravelMode(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetMotorVelocityLimits = lib.SCC_GetMotorVelocityLimits
SCC_GetMotorVelocityLimits.restype = c_short
SCC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_velocity_limits(serial_number):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SCC_GetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


SCC_GetMoveAbsolutePosition = lib.SCC_GetMoveAbsolutePosition
SCC_GetMoveAbsolutePosition.restype = c_int
SCC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def get_move_absolute_position(serial_number):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)

    output = SCC_GetMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetMoveRelativeDistance = lib.SCC_GetMoveRelativeDistance
SCC_GetMoveRelativeDistance.restype = c_int
SCC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


def get_move_relative_distance(serial_number):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)

    output = SCC_GetMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetNextMessage = lib.SCC_GetNextMessage
SCC_GetNextMessage.restype = c_bool
SCC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SCC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


SCC_GetNumberPositions = lib.SCC_GetNumberPositions
SCC_GetNumberPositions.restype = c_int
SCC_GetNumberPositions.argtypes = [POINTER(c_char)]


def get_number_positions(serial_number):
    # Get number of positions.

    serial_number = POINTER(c_char)

    output = SCC_GetNumberPositions(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetPIDLoopEncoderCoeff = lib.SCC_GetPIDLoopEncoderCoeff
SCC_GetPIDLoopEncoderCoeff.restype = c_double
SCC_GetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char)]


def get_p_i_d_loop_encoder_coeff(serial_number):
    # Gets the Encoder PID loop encoder coefficient.

    serial_number = POINTER(c_char)

    output = SCC_GetPIDLoopEncoderCoeff(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetPIDLoopEncoderParams = lib.SCC_GetPIDLoopEncoderParams
SCC_GetPIDLoopEncoderParams.restype = c_short
SCC_GetPIDLoopEncoderParams.argtypes = [POINTER(c_char), MOT_PIDLoopEncoderParams]


def get_p_i_d_loop_encoder_params(serial_number):
    # Gets the Encoder PID loop parameters.

    serial_number = POINTER(c_char)
    params = MOT_PIDLoopEncoderParams()

    output = SCC_GetPIDLoopEncoderParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


SCC_GetPosition = lib.SCC_GetPosition
SCC_GetPosition.restype = c_int
SCC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)

    output = SCC_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetPositionCounter = lib.SCC_GetPositionCounter
SCC_GetPositionCounter.restype = c_long
SCC_GetPositionCounter.argtypes = [POINTER(c_char)]


def get_position_counter(serial_number):
    # Get the Position Counter.

    serial_number = POINTER(c_char)

    output = SCC_GetPositionCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetPowerParams = lib.SCC_GetPowerParams
SCC_GetPowerParams.restype = c_short
SCC_GetPowerParams.argtypes = [POINTER(c_char), MOT_PowerParameters]


def get_power_params(serial_number):
    # Gets the power parameters for the stepper motor.

    serial_number = POINTER(c_char)
    powerParams = MOT_PowerParameters()

    output = SCC_GetPowerParams(serial_number, powerParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetRealValueFromDeviceUnit = lib.SCC_GetRealValueFromDeviceUnit
SCC_GetRealValueFromDeviceUnit.restype = c_short
SCC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = SCC_GetRealValueFromDeviceUnit(serial_number, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


SCC_GetSoftLimitMode = lib.SCC_GetSoftLimitMode
SCC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SCC_GetSoftLimitMode.argtypes = [POINTER(c_char)]


def get_soft_limit_mode(serial_number):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)

    output = SCC_GetSoftLimitMode(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetSoftwareVersion = lib.SCC_GetSoftwareVersion
SCC_GetSoftwareVersion.restype = c_ulong
SCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = SCC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetStageAxisMaxPos = lib.SCC_GetStageAxisMaxPos
SCC_GetStageAxisMaxPos.restype = c_int
SCC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


def get_stage_axis_max_pos(serial_number):
    # Gets the Stepper Motor maximum stage position.

    serial_number = POINTER(c_char)

    output = SCC_GetStageAxisMaxPos(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetStageAxisMinPos = lib.SCC_GetStageAxisMinPos
SCC_GetStageAxisMinPos.restype = c_int
SCC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


def get_stage_axis_min_pos(serial_number):
    # Gets the Stepper Motor minimum stage position.

    serial_number = POINTER(c_char)

    output = SCC_GetStageAxisMinPos(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetStatusBits = lib.SCC_GetStatusBits
SCC_GetStatusBits.restype = c_ulong
SCC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = SCC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_GetTriggerConfigParams = lib.SCC_GetTriggerConfigParams
SCC_GetTriggerConfigParams.restype = c_short
SCC_GetTriggerConfigParams.argtypes = [
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

    output = SCC_GetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


SCC_GetTriggerConfigParamsBlock = lib.SCC_GetTriggerConfigParamsBlock
SCC_GetTriggerConfigParamsBlock.restype = c_short
SCC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]


def get_trigger_config_params_block(serial_number):
    # Gets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KMOT_TriggerConfig()

    output = SCC_GetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetTriggerParamsParams = lib.SCC_GetTriggerParamsParams
SCC_GetTriggerParamsParams.restype = c_short
SCC_GetTriggerParamsParams.argtypes = [
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

    output = SCC_GetTriggerParamsParams(
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


SCC_GetTriggerParamsParamsBlock = lib.SCC_GetTriggerParamsParamsBlock
SCC_GetTriggerParamsParamsBlock.restype = c_short
SCC_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]


def get_trigger_params_params_block(serial_number):
    # Gets the trigger parameters block.

    serial_number = POINTER(c_char)
    triggerParamsParams = KMOT_TriggerParams()

    output = SCC_GetTriggerParamsParamsBlock(serial_number, triggerParamsParams)
    if output != 0:
        raise KinesisException(output)


SCC_GetVelParams = lib.SCC_GetVelParams
SCC_GetVelParams.restype = c_short
SCC_GetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_vel_params(serial_number):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_GetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SCC_GetVelParamsBlock = lib.SCC_GetVelParamsBlock
SCC_GetVelParamsBlock.restype = c_short
SCC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def get_vel_params_block(serial_number):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = SCC_GetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


SCC_HasLastMsgTimerOverrun = lib.SCC_HasLastMsgTimerOverrun
SCC_HasLastMsgTimerOverrun.restype = c_bool
SCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by SCC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = SCC_HasLastMsgTimerOverrun(serial_number)

    return output


SCC_Home = lib.SCC_Home
SCC_Home.restype = c_short
SCC_Home.argtypes = [POINTER(c_char)]


def home(serial_number):
    # Home the device.

    serial_number = POINTER(c_char)

    output = SCC_Home(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_Identify = lib.SCC_Identify
SCC_Identify.restype = c_void_p
SCC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = SCC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_IsCalibrationActive = lib.SCC_IsCalibrationActive
SCC_IsCalibrationActive.restype = c_bool
SCC_IsCalibrationActive.argtypes = [POINTER(c_char)]


def is_calibration_active(serial_number):
    # Is a calibration file active for this motor.

    serial_number = POINTER(c_char)

    output = SCC_IsCalibrationActive(serial_number)

    return output


SCC_LoadNamedSettings = lib.SCC_LoadNamedSettings
SCC_LoadNamedSettings.restype = c_bool
SCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = SCC_LoadNamedSettings(serial_number, settingsName)

    return output


SCC_LoadSettings = lib.SCC_LoadSettings
SCC_LoadSettings.restype = c_bool
SCC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = SCC_LoadSettings(serial_number)

    return output


SCC_MessageQueueSize = lib.SCC_MessageQueueSize
SCC_MessageQueueSize.restype = c_int
SCC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = SCC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_MoveAbsolute = lib.SCC_MoveAbsolute
SCC_MoveAbsolute.restype = c_short
SCC_MoveAbsolute.argtypes = [POINTER(c_char)]


def move_absolute(serial_number):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)

    output = SCC_MoveAbsolute(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_MoveAtVelocity = lib.SCC_MoveAtVelocity
SCC_MoveAtVelocity.restype = c_short
SCC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_at_velocity(serial_number):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    direction = MOT_TravelDirection()

    output = SCC_MoveAtVelocity(serial_number, direction)
    if output != 0:
        raise KinesisException(output)


SCC_MoveJog = lib.SCC_MoveJog
SCC_MoveJog.restype = c_short
SCC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_jog(serial_number):
    # Perform a jog.

    serial_number = POINTER(c_char)
    jogDirection = MOT_TravelDirection()

    output = SCC_MoveJog(serial_number, jogDirection)
    if output != 0:
        raise KinesisException(output)


SCC_MoveRelative = lib.SCC_MoveRelative
SCC_MoveRelative.restype = c_short
SCC_MoveRelative.argtypes = [POINTER(c_char), c_int]


def move_relative(serial_number):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    displacement = c_int()

    output = SCC_MoveRelative(serial_number, displacement)
    if output != 0:
        raise KinesisException(output)


SCC_MoveRelativeDistance = lib.SCC_MoveRelativeDistance
SCC_MoveRelativeDistance.restype = c_short
SCC_MoveRelativeDistance.argtypes = [POINTER(c_char)]


def move_relative_distance(serial_number):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)

    output = SCC_MoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_MoveToPosition = lib.SCC_MoveToPosition
SCC_MoveToPosition.restype = c_short
SCC_MoveToPosition.argtypes = [POINTER(c_char), c_int]


def move_to_position(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    index = c_int()

    output = SCC_MoveToPosition(serial_number, index)
    if output != 0:
        raise KinesisException(output)


SCC_NeedsHoming = lib.SCC_NeedsHoming
SCC_NeedsHoming.restype = c_bool
SCC_NeedsHoming.argtypes = [POINTER(c_char)]


def needs_homing(serial_number):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)

    output = SCC_NeedsHoming(serial_number)

    return output


SCC_Open = lib.SCC_Open
SCC_Open.restype = c_short
SCC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = SCC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_PersistSettings = lib.SCC_PersistSettings
SCC_PersistSettings.restype = c_bool
SCC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = SCC_PersistSettings(serial_number)

    return output


SCC_PollingDuration = lib.SCC_PollingDuration
SCC_PollingDuration.restype = c_long
SCC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = SCC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RegisterMessageCallback = lib.SCC_RegisterMessageCallback
SCC_RegisterMessageCallback.restype = c_void_p
SCC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = SCC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


SCC_RequestBacklash = lib.SCC_RequestBacklash
SCC_RequestBacklash.restype = c_short
SCC_RequestBacklash.argtypes = [POINTER(c_char)]


def request_backlash(serial_number):
    # Requests the backlash.

    serial_number = POINTER(c_char)

    output = SCC_RequestBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestBowIndex = lib.SCC_RequestBowIndex
SCC_RequestBowIndex.restype = c_short
SCC_RequestBowIndex.argtypes = [POINTER(c_char)]


def request_bow_index(serial_number):
    # Requests the stepper motor bow index.

    serial_number = POINTER(c_char)

    output = SCC_RequestBowIndex(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestDigitalOutputs = lib.SCC_RequestDigitalOutputs
SCC_RequestDigitalOutputs.restype = c_short
SCC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]


def request_digital_outputs(serial_number):
    # Requests the digital output bits.

    serial_number = POINTER(c_char)

    output = SCC_RequestDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestEncoderCounter = lib.SCC_RequestEncoderCounter
SCC_RequestEncoderCounter.restype = c_short
SCC_RequestEncoderCounter.argtypes = [POINTER(c_char)]


def request_encoder_counter(serial_number):
    # Requests the encoder counter.

    serial_number = POINTER(c_char)

    output = SCC_RequestEncoderCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestFrontPanelLocked = lib.SCC_RequestFrontPanelLocked
SCC_RequestFrontPanelLocked.restype = c_short
SCC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = SCC_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestHomingParams = lib.SCC_RequestHomingParams
SCC_RequestHomingParams.restype = c_short
SCC_RequestHomingParams.argtypes = [POINTER(c_char)]


def request_homing_params(serial_number):
    # Requests the homing parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestHomingParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestJogParams = lib.SCC_RequestJogParams
SCC_RequestJogParams.restype = c_short
SCC_RequestJogParams.argtypes = [POINTER(c_char)]


def request_jog_params(serial_number):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestJogParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestLimitSwitchParams = lib.SCC_RequestLimitSwitchParams
SCC_RequestLimitSwitchParams.restype = c_short
SCC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]


def request_limit_switch_params(serial_number):
    # Requests the limit switch parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestLimitSwitchParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestMMIParams = lib.SCC_RequestMMIParams
SCC_RequestMMIParams.restype = c_short
SCC_RequestMMIParams.argtypes = [POINTER(c_char)]


def request_m_m_i_params(serial_number):
    # Requests the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)

    output = SCC_RequestMMIParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestMoveAbsolutePosition = lib.SCC_RequestMoveAbsolutePosition
SCC_RequestMoveAbsolutePosition.restype = c_short
SCC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def request_move_absolute_position(serial_number):
    # Requests the position of next absolute move.

    serial_number = POINTER(c_char)

    output = SCC_RequestMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestMoveRelativeDistance = lib.SCC_RequestMoveRelativeDistance
SCC_RequestMoveRelativeDistance.restype = c_short
SCC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


def request_move_relative_distance(serial_number):
    # Requests the relative move distance.

    serial_number = POINTER(c_char)

    output = SCC_RequestMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestPIDLoopEncoderParams = lib.SCC_RequestPIDLoopEncoderParams
SCC_RequestPIDLoopEncoderParams.restype = c_short
SCC_RequestPIDLoopEncoderParams.argtypes = [POINTER(c_char)]


def request_p_i_d_loop_encoder_params(serial_number):
    # Requests the Encoder PID loop parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestPIDLoopEncoderParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestPosTriggerParams = lib.SCC_RequestPosTriggerParams
SCC_RequestPosTriggerParams.restype = c_short
SCC_RequestPosTriggerParams.argtypes = [POINTER(c_char)]


def request_pos_trigger_params(serial_number):
    # Requests the position trigger parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestPosTriggerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestPosition = lib.SCC_RequestPosition
SCC_RequestPosition.restype = c_short
SCC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current position.

    serial_number = POINTER(c_char)

    output = SCC_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestPowerParams = lib.SCC_RequestPowerParams
SCC_RequestPowerParams.restype = c_short
SCC_RequestPowerParams.argtypes = [POINTER(c_char)]


def request_power_params(serial_number):
    # Requests the power parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestPowerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestSettings = lib.SCC_RequestSettings
SCC_RequestSettings.restype = c_short
SCC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = SCC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestStatusBits = lib.SCC_RequestStatusBits
SCC_RequestStatusBits.restype = c_short
SCC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)

    output = SCC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestTriggerConfigParams = lib.SCC_RequestTriggerConfigParams
SCC_RequestTriggerConfigParams.restype = c_short
SCC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    # Requests the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestTriggerConfigParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_RequestVelParams = lib.SCC_RequestVelParams
SCC_RequestVelParams.restype = c_short
SCC_RequestVelParams.argtypes = [POINTER(c_char)]


def request_vel_params(serial_number):
    # Requests the velocity parameters.

    serial_number = POINTER(c_char)

    output = SCC_RequestVelParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_ResetRotationModes = lib.SCC_ResetRotationModes
SCC_ResetRotationModes.restype = c_short
SCC_ResetRotationModes.argtypes = [POINTER(c_char)]


def reset_rotation_modes(serial_number):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)

    output = SCC_ResetRotationModes(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_ResumeMoveMessages = lib.SCC_ResumeMoveMessages
SCC_ResumeMoveMessages.restype = c_short
SCC_ResumeMoveMessages.argtypes = [POINTER(c_char)]


def resume_move_messages(serial_number):
    # Resume suspended move messages.

    serial_number = POINTER(c_char)

    output = SCC_ResumeMoveMessages(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_SetBacklash = lib.SCC_SetBacklash
SCC_SetBacklash.restype = c_short
SCC_SetBacklash.argtypes = [POINTER(c_char), c_long]


def set_backlash(serial_number):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    distance = c_long()

    output = SCC_SetBacklash(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


SCC_SetBowIndex = lib.SCC_SetBowIndex
SCC_SetBowIndex.restype = c_short
SCC_SetBowIndex.argtypes = [POINTER(c_char), c_short]


def set_bow_index(serial_number):
    # Sets the stepper motor bow index.

    serial_number = POINTER(c_char)
    bowIndex = c_short()

    output = SCC_SetBowIndex(serial_number, bowIndex)
    if output != 0:
        raise KinesisException(output)


SCC_SetCalibrationFile = lib.SCC_SetCalibrationFile
SCC_SetCalibrationFile.restype = c_void_p
SCC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_bool]


def set_calibration_file(serial_number):
    # Set the calibration file for this motor.

    serial_number = POINTER(c_char)
    filename = POINTER(c_char)
    enabled = c_bool()

    output = SCC_SetCalibrationFile(serial_number, filename, enabled)
    if output != 0:
        raise KinesisException(output)


SCC_SetDigitalOutputs = lib.SCC_SetDigitalOutputs
SCC_SetDigitalOutputs.restype = c_short
SCC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]


def set_digital_outputs(serial_number):
    # Sets the digital output bits.

    serial_number = POINTER(c_char)
    outputsBits = c_byte()

    output = SCC_SetDigitalOutputs(serial_number, outputsBits)
    if output != 0:
        raise KinesisException(output)


SCC_SetDirection = lib.SCC_SetDirection
SCC_SetDirection.restype = c_void_p
SCC_SetDirection.argtypes = [POINTER(c_char), c_bool]


def set_direction(serial_number):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    reverse = c_bool()

    output = SCC_SetDirection(serial_number, reverse)
    if output != 0:
        raise KinesisException(output)


SCC_SetEncoderCounter = lib.SCC_SetEncoderCounter
SCC_SetEncoderCounter.restype = c_short
SCC_SetEncoderCounter.argtypes = [POINTER(c_char), c_long]


def set_encoder_counter(serial_number):
    # Set the Encoder Counter values.

    serial_number = POINTER(c_char)
    count = c_long()

    output = SCC_SetEncoderCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


SCC_SetFrontPanelLock = lib.SCC_SetFrontPanelLock
SCC_SetFrontPanelLock.restype = c_short
SCC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = SCC_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


SCC_SetHomingParamsBlock = lib.SCC_SetHomingParamsBlock
SCC_SetHomingParamsBlock.restype = c_short
SCC_SetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def set_homing_params_block(serial_number):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = SCC_SetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetHomingVelocity = lib.SCC_SetHomingVelocity
SCC_SetHomingVelocity.restype = c_short
SCC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]


def set_homing_velocity(serial_number):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    velocity = c_uint()

    output = SCC_SetHomingVelocity(serial_number, velocity)
    if output != 0:
        raise KinesisException(output)


SCC_SetJogMode = lib.SCC_SetJogMode
SCC_SetJogMode.restype = c_short
SCC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SCC_SetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


SCC_SetJogParamsBlock = lib.SCC_SetJogParamsBlock
SCC_SetJogParamsBlock.restype = c_short
SCC_SetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def set_jog_params_block(serial_number):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = SCC_SetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetJogStepSize = lib.SCC_SetJogStepSize
SCC_SetJogStepSize.restype = c_short
SCC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]


def set_jog_step_size(serial_number):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    stepSize = c_uint()

    output = SCC_SetJogStepSize(serial_number, stepSize)
    if output != 0:
        raise KinesisException(output)


SCC_SetJogVelParams = lib.SCC_SetJogVelParams
SCC_SetJogVelParams.restype = c_short
SCC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_jog_vel_params(serial_number):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_SetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SCC_SetLimitSwitchParams = lib.SCC_SetLimitSwitchParams
SCC_SetLimitSwitchParams.restype = c_short
SCC_SetLimitSwitchParams.argtypes = [
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

    output = SCC_SetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


SCC_SetLimitSwitchParamsBlock = lib.SCC_SetLimitSwitchParamsBlock
SCC_SetLimitSwitchParamsBlock.restype = c_short
SCC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def set_limit_switch_params_block(serial_number):
    # Set the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SCC_SetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetLimitsSoftwareApproachPolicy = lib.SCC_SetLimitsSoftwareApproachPolicy
SCC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SCC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = SCC_SetLimitsSoftwareApproachPolicy(serial_number, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


SCC_SetMMIParams = lib.SCC_SetMMIParams
SCC_SetMMIParams.restype = c_short
SCC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KMOT_WheelMode,
    c_int32,
    c_int32,
    KMOT_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def set_m_m_i_params(serial_number):
    # Set the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = SCC_SetMMIParams(
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


SCC_SetMMIParamsBlock = lib.SCC_SetMMIParamsBlock
SCC_SetMMIParamsBlock.restype = c_short
SCC_SetMMIParamsBlock.argtypes = [POINTER(c_char), KMOT_MMIParams]


def set_m_m_i_params_block(serial_number):
    # Sets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KMOT_MMIParams()

    output = SCC_SetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetMMIParamsExt = lib.SCC_SetMMIParamsExt
SCC_SetMMIParamsExt.restype = c_short
SCC_SetMMIParamsExt.argtypes = [
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
    # Set the MMI Parameters for the KCube Display Interface.

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

    output = SCC_SetMMIParamsExt(
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


SCC_SetMotorParams = lib.SCC_SetMotorParams
SCC_SetMotorParams.restype = c_short
SCC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def set_motor_params(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SCC_SetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SCC_SetMotorParamsExt = lib.SCC_SetMotorParamsExt
SCC_SetMotorParamsExt.restype = c_short
SCC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def set_motor_params_ext(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SCC_SetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


SCC_SetMotorTravelLimits = lib.SCC_SetMotorTravelLimits
SCC_SetMotorTravelLimits.restype = c_short
SCC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_travel_limits(serial_number):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = SCC_SetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


SCC_SetMotorTravelMode = lib.SCC_SetMotorTravelMode
SCC_SetMotorTravelMode.restype = c_short
SCC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]


def set_motor_travel_mode(serial_number):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    travelMode = MOT_TravelModes()

    output = SCC_SetMotorTravelMode(serial_number, travelMode)
    if output != 0:
        raise KinesisException(output)


SCC_SetMotorVelocityLimits = lib.SCC_SetMotorVelocityLimits
SCC_SetMotorVelocityLimits.restype = c_short
SCC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_velocity_limits(serial_number):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SCC_SetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


SCC_SetMoveAbsolutePosition = lib.SCC_SetMoveAbsolutePosition
SCC_SetMoveAbsolutePosition.restype = c_short
SCC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]


def set_move_absolute_position(serial_number):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    position = c_int()

    output = SCC_SetMoveAbsolutePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


SCC_SetMoveRelativeDistance = lib.SCC_SetMoveRelativeDistance
SCC_SetMoveRelativeDistance.restype = c_short
SCC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]


def set_move_relative_distance(serial_number):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    distance = c_int()

    output = SCC_SetMoveRelativeDistance(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


SCC_SetPIDLoopEncoderCoeff = lib.SCC_SetPIDLoopEncoderCoeff
SCC_SetPIDLoopEncoderCoeff.restype = c_short
SCC_SetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char), c_double]


def set_p_i_d_loop_encoder_coeff(serial_number):
    # Sets the Encoder PID loop encoder coefficient.

    serial_number = POINTER(c_char)
    coeff = c_double()

    output = SCC_SetPIDLoopEncoderCoeff(serial_number, coeff)
    if output != 0:
        raise KinesisException(output)


SCC_SetPIDLoopEncoderParams = lib.SCC_SetPIDLoopEncoderParams
SCC_SetPIDLoopEncoderParams.restype = c_short
SCC_SetPIDLoopEncoderParams.argtypes = [POINTER(c_char), MOT_PIDLoopEncoderParams]


def set_p_i_d_loop_encoder_params(serial_number):
    # Sets the Encoder PID loop parameters.

    serial_number = POINTER(c_char)
    params = MOT_PIDLoopEncoderParams()

    output = SCC_SetPIDLoopEncoderParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


SCC_SetPositionCounter = lib.SCC_SetPositionCounter
SCC_SetPositionCounter.restype = c_short
SCC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]


def set_position_counter(serial_number):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    count = c_long()

    output = SCC_SetPositionCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


SCC_SetPowerParams = lib.SCC_SetPowerParams
SCC_SetPowerParams.restype = c_short
SCC_SetPowerParams.argtypes = [POINTER(c_char), MOT_PowerParameters]


def set_power_params(serial_number):
    # Sets the power parameters for the stepper motor.

    serial_number = POINTER(c_char)
    powerParams = MOT_PowerParameters()

    output = SCC_SetPowerParams(serial_number, powerParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetRotationModes = lib.SCC_SetRotationModes
SCC_SetRotationModes.restype = c_short
SCC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = SCC_SetRotationModes(serial_number, mode, direction)
    if output != 0:
        raise KinesisException(output)


SCC_SetStageAxisLimits = lib.SCC_SetStageAxisLimits
SCC_SetStageAxisLimits.restype = c_short
SCC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]


def set_stage_axis_limits(serial_number):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    minPosition = c_int()
    maxPosition = c_int()

    output = SCC_SetStageAxisLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


SCC_SetStageType = lib.SCC_SetStageType
SCC_SetStageType.restype = c_short
SCC_SetStageType.argtypes = [POINTER(c_char), KST_Stages, TST_Stages]


def set_stage_type(serial_number):
    # Sets the stage type.

    serial_number = POINTER(c_char)
    stageId = KST_Stages()
    stageId = TST_Stages()

    output = SCC_SetStageType(serial_number, stageId, stageId)
    if output != 0:
        raise KinesisException(output)


SCC_SetTriggerConfigParams = lib.SCC_SetTriggerConfigParams
SCC_SetTriggerConfigParams.restype = c_short
SCC_SetTriggerConfigParams.argtypes = [
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

    output = SCC_SetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


SCC_SetTriggerConfigParamsBlock = lib.SCC_SetTriggerConfigParamsBlock
SCC_SetTriggerConfigParamsBlock.restype = c_short
SCC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerConfig]


def set_trigger_config_params_block(serial_number):
    # Sets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KMOT_TriggerConfig()

    output = SCC_SetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetTriggerParamsParams = lib.SCC_SetTriggerParamsParams
SCC_SetTriggerParamsParams.restype = c_short
SCC_SetTriggerParamsParams.argtypes = [
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

    output = SCC_SetTriggerParamsParams(
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


SCC_SetTriggerParamsParamsBlock = lib.SCC_SetTriggerParamsParamsBlock
SCC_SetTriggerParamsParamsBlock.restype = c_short
SCC_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char), KMOT_TriggerParams]


def set_trigger_params_params_block(serial_number):
    # Sets the trigger parameters block.

    serial_number = POINTER(c_char)
    triggerParamsParams = KMOT_TriggerParams()

    output = SCC_SetTriggerParamsParamsBlock(serial_number, triggerParamsParams)
    if output != 0:
        raise KinesisException(output)


SCC_SetVelParams = lib.SCC_SetVelParams
SCC_SetVelParams.restype = c_short
SCC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_vel_params(serial_number):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_SetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


SCC_SetVelParamsBlock = lib.SCC_SetVelParamsBlock
SCC_SetVelParamsBlock.restype = c_short
SCC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def set_vel_params_block(serial_number):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = SCC_SetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


SCC_StartPolling = lib.SCC_StartPolling
SCC_StartPolling.restype = c_bool
SCC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = SCC_StartPolling(serial_number, milliseconds)

    return output


SCC_StopImmediate = lib.SCC_StopImmediate
SCC_StopImmediate.restype = c_short
SCC_StopImmediate.argtypes = [POINTER(c_char)]


def stop_immediate(serial_number):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)

    output = SCC_StopImmediate(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_StopPolling = lib.SCC_StopPolling
SCC_StopPolling.restype = c_void_p
SCC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = SCC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_StopProfiled = lib.SCC_StopProfiled
SCC_StopProfiled.restype = c_short
SCC_StopProfiled.argtypes = [POINTER(c_char)]


def stop_profiled(serial_number):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)

    output = SCC_StopProfiled(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_SuspendMoveMessages = lib.SCC_SuspendMoveMessages
SCC_SuspendMoveMessages.restype = c_short
SCC_SuspendMoveMessages.argtypes = [POINTER(c_char)]


def suspend_move_messages(serial_number):
    # Suspend automatic messages at ends of moves.

    serial_number = POINTER(c_char)

    output = SCC_SuspendMoveMessages(serial_number)
    if output != 0:
        raise KinesisException(output)


SCC_TimeSinceLastMsgReceived = lib.SCC_TimeSinceLastMsgReceived
SCC_TimeSinceLastMsgReceived.restype = c_bool
SCC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = SCC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


SCC_UsesPIDLoopEncoding = lib.SCC_UsesPIDLoopEncoding
SCC_UsesPIDLoopEncoding.restype = c_bool
SCC_UsesPIDLoopEncoding.argtypes = [POINTER(c_char)]


def uses_p_i_d_loop_encoding(serial_number):
    # Determines if we can uses PID loop encoding.

    serial_number = POINTER(c_char)

    output = SCC_UsesPIDLoopEncoding(serial_number)

    return output


SCC_WaitForMessage = lib.SCC_WaitForMessage
SCC_WaitForMessage.restype = c_bool
SCC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SCC_WaitForMessage(serial_number, messageType, messageID, messageData)

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
