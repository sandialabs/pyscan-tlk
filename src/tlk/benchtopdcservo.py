from ctypes import (
    POINTER,
    c_bool,
    c_byte,
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
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
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
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_DC_PIDParameters,
    MOT_EncoderResolutionParams,
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
    lib_path + "Thorlabs.MotionControl.Benchtop.DCServo.dll")

BDC_CanHome = lib.BDC_CanHome
BDC_CanHome.restype = c_bool
BDC_CanHome.argtypes = [POINTER(c_char), c_short]


def can_home(serial_number, channel):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_CanHome(serial_number, channel)

    return output


BDC_CanMoveWithoutHomingFirst = lib.BDC_CanMoveWithoutHomingFirst
BDC_CanMoveWithoutHomingFirst.restype = c_bool
BDC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]


def can_move_without_homing_first(serial_number, channel):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_CanMoveWithoutHomingFirst(serial_number, channel)

    return output


BDC_CheckConnection = lib.BDC_CheckConnection
BDC_CheckConnection.restype = c_bool
BDC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = BDC_CheckConnection(serial_number)

    return output


BDC_ClearMessageQueue = lib.BDC_ClearMessageQueue
BDC_ClearMessageQueue.restype = c_short
BDC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]


def clear_message_queue(serial_number, channel):
    # Clears the device message queue.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_ClearMessageQueue(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_Close = lib.BDC_Close
BDC_Close.restype = c_short
BDC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = BDC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_DisableChannel = lib.BDC_DisableChannel
BDC_DisableChannel.restype = c_short
BDC_DisableChannel.argtypes = [POINTER(c_char), c_short]


def disable_channel(serial_number, channel):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_DisableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_EnableChannel = lib.BDC_EnableChannel
BDC_EnableChannel.restype = c_short
BDC_EnableChannel.argtypes = [POINTER(c_char), c_short]


def enable_channel(serial_number, channel):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_EnableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_EnableLastMsgTimer = lib.BDC_EnableLastMsgTimer
BDC_EnableLastMsgTimer.restype = c_void_p
BDC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]


def enable_last_msg_timer(serial_number, channel):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = BDC_EnableLastMsgTimer(serial_number, channel, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


BDC_GetBacklash = lib.BDC_GetBacklash
BDC_GetBacklash.restype = c_long
BDC_GetBacklash.argtypes = [POINTER(c_char), c_short]


def get_backlash(serial_number, channel):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetBacklash(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetCalibrationFile = lib.BDC_GetCalibrationFile
BDC_GetCalibrationFile.restype = c_bool
BDC_GetCalibrationFile.argtypes = [POINTER(c_char), c_short, POINTER(c_char), c_short]


def get_calibration_file(serial_number, channel):
    # Get calibration file for this motor.

    serial_number = POINTER(c_char)
    channel = c_short()
    filename = POINTER(c_char)
    sizeOfBuffer = c_short()

    output = BDC_GetCalibrationFile(serial_number, channel, filename, sizeOfBuffer)

    return output


BDC_GetDCPIDParams = lib.BDC_GetDCPIDParams
BDC_GetDCPIDParams.restype = c_short
BDC_GetDCPIDParams.argtypes = [POINTER(c_char), MOT_DC_PIDParameters, c_short]


def get_d_c_p_i_d_params(serial_number, channel):
    # Gets the DC PID parameters.

    serial_number = POINTER(c_char)
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()
    channel = c_short()

    output = BDC_GetDCPIDParams(serial_number, DCproportionalIntegralDerivativeParams, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetDeviceUnitFromRealValue = lib.BDC_GetDeviceUnitFromRealValue
BDC_GetDeviceUnitFromRealValue.restype = c_short
BDC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_short, c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number, channel):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    channel = c_short()
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = BDC_GetDeviceUnitFromRealValue(serial_number, channel, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


BDC_GetDigitalOutputs = lib.BDC_GetDigitalOutputs
BDC_GetDigitalOutputs.restype = c_byte
BDC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]


def get_digital_outputs(serial_number, channel):
    # Gets the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetDigitalOutputs(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetEncoderCounter = lib.BDC_GetEncoderCounter
BDC_GetEncoderCounter.restype = c_long
BDC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]


def get_encoder_counter(serial_number, channel):
    # Get the Encoder Counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetEncoderCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetEncoderResolutionParams = lib.BDC_GetEncoderResolutionParams
BDC_GetEncoderResolutionParams.restype = c_short
BDC_GetEncoderResolutionParams.argtypes = [POINTER(c_char), c_short, MOT_EncoderResolutionParams]


def get_encoder_resolution_params(serial_number, channel):
    # Get the encoder resolution parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    resolutionParams = MOT_EncoderResolutionParams()

    output = BDC_GetEncoderResolutionParams(serial_number, channel, resolutionParams)
    if output != 0:
        raise KinesisException(output)


BDC_GetFirmwareVersion = lib.BDC_GetFirmwareVersion
BDC_GetFirmwareVersion.restype = c_ulong
BDC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]


def get_firmware_version(serial_number, channel):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetFirmwareVersion(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetHardwareInfo = lib.BDC_GetHardwareInfo
BDC_GetHardwareInfo.restype = c_short
BDC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    c_short,
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]


def get_hardware_info(serial_number, channel):
    # Gets the hardware information from the device.

    serial_number = POINTER(c_char)
    channel = c_short()
    modelNo = POINTER(c_char)
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = BDC_GetHardwareInfo(
        serial_number,
        channel,
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


BDC_GetHardwareInfoBlock = lib.BDC_GetHardwareInfoBlock
BDC_GetHardwareInfoBlock.restype = c_short
BDC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), c_short, TLI_HardwareInformation]


def get_hardware_info_block(serial_number, channel):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    channel = c_short()
    hardwareInfo = TLI_HardwareInformation()

    output = BDC_GetHardwareInfoBlock(serial_number, channel, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


BDC_GetHomingParamsBlock = lib.BDC_GetHomingParamsBlock
BDC_GetHomingParamsBlock.restype = c_short
BDC_GetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


def get_homing_params_block(serial_number, channel):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = BDC_GetHomingParamsBlock(serial_number, channel, homingParams)
    if output != 0:
        raise KinesisException(output)


BDC_GetHomingVelocity = lib.BDC_GetHomingVelocity
BDC_GetHomingVelocity.restype = c_uint
BDC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]


def get_homing_velocity(serial_number, channel):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetHomingVelocity(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetInputVoltage = lib.BDC_GetInputVoltage
BDC_GetInputVoltage.restype = c_long
BDC_GetInputVoltage.argtypes = [POINTER(c_char), c_short]


def get_input_voltage(serial_number, channel):
    # Gets the analogue input voltage reading.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetInputVoltage(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetJogMode = lib.BDC_GetJogMode
BDC_GetJogMode.restype = c_short
BDC_GetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number, channel):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BDC_GetJogMode(serial_number, channel, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


BDC_GetJogParamsBlock = lib.BDC_GetJogParamsBlock
BDC_GetJogParamsBlock.restype = c_short
BDC_GetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters]


def get_jog_params_block(serial_number, channel):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogParams = MOT_JogParameters()

    output = BDC_GetJogParamsBlock(serial_number, channel, jogParams)
    if output != 0:
        raise KinesisException(output)


BDC_GetJogStepSize = lib.BDC_GetJogStepSize
BDC_GetJogStepSize.restype = c_uint
BDC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]


def get_jog_step_size(serial_number, channel):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetJogStepSize(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetJogVelParams = lib.BDC_GetJogVelParams
BDC_GetJogVelParams.restype = c_short
BDC_GetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def get_jog_vel_params(serial_number, channel):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BDC_GetJogVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BDC_GetLimitSwitchParams = lib.BDC_GetLimitSwitchParams
BDC_GetLimitSwitchParams.restype = c_short
BDC_GetLimitSwitchParams.argtypes = [
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

    output = BDC_GetLimitSwitchParams(
        serial_number,
        channel,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


BDC_GetLimitSwitchParamsBlock = lib.BDC_GetLimitSwitchParamsBlock
BDC_GetLimitSwitchParamsBlock.restype = c_short
BDC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LimitSwitchParameters]


def get_limit_switch_params_block(serial_number, channel):
    # Get the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = BDC_GetLimitSwitchParamsBlock(serial_number, channel, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


BDC_GetMotorParams = lib.BDC_GetMotorParams
BDC_GetMotorParams.restype = c_short
BDC_GetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_float]


def get_motor_params(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = BDC_GetMotorParams(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BDC_GetMotorParamsExt = lib.BDC_GetMotorParamsExt
BDC_GetMotorParamsExt.restype = c_short
BDC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]


def get_motor_params_ext(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = BDC_GetMotorParamsExt(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BDC_GetMotorTravelLimits = lib.BDC_GetMotorTravelLimits
BDC_GetMotorTravelLimits.restype = c_short
BDC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def get_motor_travel_limits(serial_number, channel):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = BDC_GetMotorTravelLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BDC_GetMotorTravelMode = lib.BDC_GetMotorTravelMode
BDC_GetMotorTravelMode.restype = MOT_TravelModes
BDC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]


def get_motor_travel_mode(serial_number, channel):
    # Get the motor travel mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetMotorTravelMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetMotorVelocityLimits = lib.BDC_GetMotorVelocityLimits
BDC_GetMotorVelocityLimits.restype = c_short
BDC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def get_motor_velocity_limits(serial_number, channel):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BDC_GetMotorVelocityLimits(serial_number, channel, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


BDC_GetMoveAbsolutePosition = lib.BDC_GetMoveAbsolutePosition
BDC_GetMoveAbsolutePosition.restype = c_int
BDC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


def get_move_absolute_position(serial_number, channel):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetMoveAbsolutePosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetMoveRelativeDistance = lib.BDC_GetMoveRelativeDistance
BDC_GetMoveRelativeDistance.restype = c_int
BDC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def get_move_relative_distance(serial_number, channel):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetMoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetNextMessage = lib.BDC_GetNextMessage
BDC_GetNextMessage.restype = c_bool
BDC_GetNextMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


def get_next_message(serial_number, channel):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BDC_GetNextMessage(serial_number, channel, messageType, messageID, messageData)

    return output


BDC_GetNumChannels = lib.BDC_GetNumChannels
BDC_GetNumChannels.restype = c_short
BDC_GetNumChannels.argtypes = [POINTER(c_char)]


def get_num_channels(serial_number):
    # Gets the number of channels in the device.

    serial_number = POINTER(c_char)

    output = BDC_GetNumChannels(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_GetNumberPositions = lib.BDC_GetNumberPositions
BDC_GetNumberPositions.restype = c_int
BDC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]


def get_number_positions(serial_number, channel):
    # Get number of positions.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetNumberPositions(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetPosition = lib.BDC_GetPosition
BDC_GetPosition.restype = c_int
BDC_GetPosition.argtypes = [POINTER(c_char), c_short]


def get_position(serial_number, channel):
    # Get the current position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetPositionCounter = lib.BDC_GetPositionCounter
BDC_GetPositionCounter.restype = c_long
BDC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]


def get_position_counter(serial_number, channel):
    # Get the Position Counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetPositionCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetRackDigitalOutputs = lib.BDC_GetRackDigitalOutputs
BDC_GetRackDigitalOutputs.restype = c_byte
BDC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def get_rack_digital_outputs(serial_number):
    # Gets the rack digital output bits.

    serial_number = POINTER(c_char)

    output = BDC_GetRackDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_GetRackStatusBits = lib.BDC_GetRackStatusBits
BDC_GetRackStatusBits.restype = c_ulong
BDC_GetRackStatusBits.argtypes = [POINTER(c_char)]


def get_rack_status_bits(serial_number):
    # Gets the Rack status bits.

    serial_number = POINTER(c_char)

    output = BDC_GetRackStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_GetRealValueFromDeviceUnit = lib.BDC_GetRealValueFromDeviceUnit
BDC_GetRealValueFromDeviceUnit.restype = c_short
BDC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_short, c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number, channel):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    channel = c_short()
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = BDC_GetRealValueFromDeviceUnit(serial_number, channel, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


BDC_GetSoftLimitMode = lib.BDC_GetSoftLimitMode
BDC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BDC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]


def get_soft_limit_mode(serial_number, channel):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetSoftLimitMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetSoftwareVersion = lib.BDC_GetSoftwareVersion
BDC_GetSoftwareVersion.restype = c_ulong
BDC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = BDC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_GetStageAxisMaxPos = lib.BDC_GetStageAxisMaxPos
BDC_GetStageAxisMaxPos.restype = c_int
BDC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]


def get_stage_axis_max_pos(serial_number, channel):
    # Gets the DC Servo maximum stage position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetStageAxisMaxPos(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetStageAxisMinPos = lib.BDC_GetStageAxisMinPos
BDC_GetStageAxisMinPos.restype = c_int
BDC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]


def get_stage_axis_min_pos(serial_number, channel):
    # Gets the DC Servo minimum stage position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetStageAxisMinPos(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetStatusBits = lib.BDC_GetStatusBits
BDC_GetStatusBits.restype = c_ulong
BDC_GetStatusBits.argtypes = [POINTER(c_char), c_short]


def get_status_bits(serial_number, channel):
    # Get the current status bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetTriggerConfigParams = lib.BDC_GetTriggerConfigParams
BDC_GetTriggerConfigParams.restype = c_short
BDC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    c_short,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]


def get_trigger_config_params(serial_number, channel):
    # Gets the trigger configuration parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BDC_GetTriggerConfigParams(
        serial_number,
        channel,
        trigger1Mode,
        trigger1Polarity,
        trigger2Mode,
        trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


BDC_GetTriggerConfigParamsBlock = lib.BDC_GetTriggerConfigParamsBlock
BDC_GetTriggerConfigParamsBlock.restype = c_short
BDC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), c_short, KMOT_TriggerConfig]


def get_trigger_config_params_block(serial_number, channel):
    # Gets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    channel = c_short()
    triggerConfigParams = KMOT_TriggerConfig()

    output = BDC_GetTriggerConfigParamsBlock(serial_number, channel, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


BDC_GetTriggerParams = lib.BDC_GetTriggerParams
BDC_GetTriggerParams.restype = c_short
BDC_GetTriggerParams.argtypes = [
    POINTER(c_char),
    c_short,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]


def get_trigger_params(serial_number, channel):
    # Gets the trigger parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BDC_GetTriggerParams(
        serial_number,
        channel,
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


BDC_GetTriggerParamsBlock = lib.BDC_GetTriggerParamsBlock
BDC_GetTriggerParamsBlock.restype = c_short
BDC_GetTriggerParamsBlock.argtypes = [POINTER(c_char), c_short, KMOT_TriggerParams]


def get_trigger_params_block(serial_number, channel):
    # Gets the trigger parameters block.

    serial_number = POINTER(c_char)
    channel = c_short()
    triggerParams = KMOT_TriggerParams()

    output = BDC_GetTriggerParamsBlock(serial_number, channel, triggerParams)
    if output != 0:
        raise KinesisException(output)


BDC_GetTriggerSwitches = lib.BDC_GetTriggerSwitches
BDC_GetTriggerSwitches.restype = c_byte
BDC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]


def get_trigger_switches(serial_number, channel):
    # Gets the trigger switch parameter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_GetTriggerSwitches(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_GetVelParams = lib.BDC_GetVelParams
BDC_GetVelParams.restype = c_short
BDC_GetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def get_vel_params(serial_number, channel):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BDC_GetVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BDC_GetVelParamsBlock = lib.BDC_GetVelParamsBlock
BDC_GetVelParamsBlock.restype = c_short
BDC_GetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters]


def get_vel_params_block(serial_number, channel):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()

    output = BDC_GetVelParamsBlock(serial_number, channel, velocityParams)
    if output != 0:
        raise KinesisException(output)


BDC_HasLastMsgTimerOverrun = lib.BDC_HasLastMsgTimerOverrun
BDC_HasLastMsgTimerOverrun.restype = c_bool
BDC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]


def has_last_msg_timer_overrun(serial_number, channel):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by BDC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_HasLastMsgTimerOverrun(serial_number, channel)

    return output


BDC_Home = lib.BDC_Home
BDC_Home.restype = c_short
BDC_Home.argtypes = [POINTER(c_char), c_short]


def home(serial_number, channel):
    # Home the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_Home(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_Identify = lib.BDC_Identify
BDC_Identify.restype = c_short
BDC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = BDC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_IsCalibrationActive = lib.BDC_IsCalibrationActive
BDC_IsCalibrationActive.restype = c_bool
BDC_IsCalibrationActive.argtypes = [POINTER(c_char), c_short]


def is_calibration_active(serial_number, channel):
    # Is a calibration file active for this motor.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_IsCalibrationActive(serial_number, channel)

    return output


BDC_IsChannelValid = lib.BDC_IsChannelValid
BDC_IsChannelValid.restype = c_bool
BDC_IsChannelValid.argtypes = [POINTER(c_char), c_short]


def is_channel_valid(serial_number, channel):
    # Verifies that the specified channel is valid.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_IsChannelValid(serial_number, channel)

    return output


BDC_LoadNamedSettings = lib.BDC_LoadNamedSettings
BDC_LoadNamedSettings.restype = c_bool
BDC_LoadNamedSettings.argtypes = [POINTER(c_char), c_short, POINTER(c_char)]


def load_named_settings(serial_number, channel):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    channel = c_short()
    settingsName = POINTER(c_char)

    output = BDC_LoadNamedSettings(serial_number, channel, settingsName)

    return output


BDC_LoadSettings = lib.BDC_LoadSettings
BDC_LoadSettings.restype = c_bool
BDC_LoadSettings.argtypes = [POINTER(c_char), c_short]


def load_settings(serial_number, channel):
    # Update device with stored settings.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_LoadSettings(serial_number, channel)

    return output


BDC_MaxChannelCount = lib.BDC_MaxChannelCount
BDC_MaxChannelCount.restype = c_int
BDC_MaxChannelCount.argtypes = [POINTER(c_char)]


def max_channel_count(serial_number):
    # Gets the number of channels available to this device.

    serial_number = POINTER(c_char)

    output = BDC_MaxChannelCount(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_MessageQueueSize = lib.BDC_MessageQueueSize
BDC_MessageQueueSize.restype = c_int
BDC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]


def message_queue_size(serial_number, channel):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_MessageQueueSize(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_MoveAbsolute = lib.BDC_MoveAbsolute
BDC_MoveAbsolute.restype = c_short
BDC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]


def move_absolute(serial_number, channel):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_MoveAbsolute(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_MoveAtVelocity = lib.BDC_MoveAtVelocity
BDC_MoveAtVelocity.restype = c_short
BDC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


def move_at_velocity(serial_number, channel):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    channel = c_short()
    direction = MOT_TravelDirection()

    output = BDC_MoveAtVelocity(serial_number, channel, direction)
    if output != 0:
        raise KinesisException(output)


BDC_MoveJog = lib.BDC_MoveJog
BDC_MoveJog.restype = c_short
BDC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


def move_jog(serial_number, channel):
    # Perform a jog.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogDirection = MOT_TravelDirection()

    output = BDC_MoveJog(serial_number, channel, jogDirection)
    if output != 0:
        raise KinesisException(output)


BDC_MoveRelative = lib.BDC_MoveRelative
BDC_MoveRelative.restype = c_short
BDC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]


def move_relative(serial_number, channel):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    channel = c_short()
    displacement = c_int()

    output = BDC_MoveRelative(serial_number, channel, displacement)
    if output != 0:
        raise KinesisException(output)


BDC_MoveRelativeDistance = lib.BDC_MoveRelativeDistance
BDC_MoveRelativeDistance.restype = c_short
BDC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def move_relative_distance(serial_number, channel):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_MoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_MoveToPosition = lib.BDC_MoveToPosition
BDC_MoveToPosition.restype = c_short
BDC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]


def move_to_position(serial_number, channel):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    channel = c_short()
    index = c_int()

    output = BDC_MoveToPosition(serial_number, channel, index)
    if output != 0:
        raise KinesisException(output)


BDC_NeedsHoming = lib.BDC_NeedsHoming
BDC_NeedsHoming.restype = c_bool
BDC_NeedsHoming.argtypes = [POINTER(c_char), c_short]


def needs_homing(serial_number, channel):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_NeedsHoming(serial_number, channel)

    return output


BDC_Open = lib.BDC_Open
BDC_Open.restype = c_short
BDC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = BDC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_PersistSettings = lib.BDC_PersistSettings
BDC_PersistSettings.restype = c_bool
BDC_PersistSettings.argtypes = [POINTER(c_char), c_short]


def persist_settings(serial_number, channel):
    # Persist device settings to device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_PersistSettings(serial_number, channel)

    return output


BDC_PollingDuration = lib.BDC_PollingDuration
BDC_PollingDuration.restype = c_long
BDC_PollingDuration.argtypes = [POINTER(c_char), c_short]


def polling_duration(serial_number, channel):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_PollingDuration(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RegisterMessageCallback = lib.BDC_RegisterMessageCallback
BDC_RegisterMessageCallback.restype = c_short
BDC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, c_void_p]


def register_message_callback(serial_number, channel):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    channel = c_short()
    void = c_void_p()

    output = BDC_RegisterMessageCallback(serial_number, channel, void)
    if output != 0:
        raise KinesisException(output)


BDC_RequestBacklash = lib.BDC_RequestBacklash
BDC_RequestBacklash.restype = c_short
BDC_RequestBacklash.argtypes = [POINTER(c_char), c_short]


def request_backlash(serial_number, channel):
    # Requests the backlash.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestBacklash(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestDCPIDParams = lib.BDC_RequestDCPIDParams
BDC_RequestDCPIDParams.restype = c_short
BDC_RequestDCPIDParams.argtypes = [POINTER(c_char), c_short]


def request_d_c_p_i_d_params(serial_number, channel):
    # Requests the PID parameters for DC motors used in an algorithm involving calculus.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestDCPIDParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestDigitalOutputs = lib.BDC_RequestDigitalOutputs
BDC_RequestDigitalOutputs.restype = c_short
BDC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]


def request_digital_outputs(serial_number, channel):
    # Requests the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestDigitalOutputs(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestEncoderCounter = lib.BDC_RequestEncoderCounter
BDC_RequestEncoderCounter.restype = c_short
BDC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]


def request_encoder_counter(serial_number, channel):
    # Requests the encoder counter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestEncoderCounter(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestEncoderResolutionParams = lib.BDC_RequestEncoderResolutionParams
BDC_RequestEncoderResolutionParams.restype = c_short
BDC_RequestEncoderResolutionParams.argtypes = [POINTER(c_char), c_short]


def request_encoder_resolution_params(serial_number, channel):
    # Requests the encoder resolution parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestEncoderResolutionParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestHomingParams = lib.BDC_RequestHomingParams
BDC_RequestHomingParams.restype = c_short
BDC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]


def request_homing_params(serial_number, channel):
    # Requests the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestHomingParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestInputVoltage = lib.BDC_RequestInputVoltage
BDC_RequestInputVoltage.restype = c_short
BDC_RequestInputVoltage.argtypes = [POINTER(c_char), c_short]


def request_input_voltage(serial_number, channel):
    # Requests the analogue input voltage reading.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestInputVoltage(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestJogParams = lib.BDC_RequestJogParams
BDC_RequestJogParams.restype = c_short
BDC_RequestJogParams.argtypes = [POINTER(c_char), c_short]


def request_jog_params(serial_number, channel):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestJogParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestLimitSwitchParams = lib.BDC_RequestLimitSwitchParams
BDC_RequestLimitSwitchParams.restype = c_short
BDC_RequestLimitSwitchParams.argtypes = [POINTER(c_char), c_short]


def request_limit_switch_params(serial_number, channel):
    # Requests the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestLimitSwitchParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestMoveAbsolutePosition = lib.BDC_RequestMoveAbsolutePosition
BDC_RequestMoveAbsolutePosition.restype = c_short
BDC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


def request_move_absolute_position(serial_number, channel):
    # Requests the position of next absolute move.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestMoveAbsolutePosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestMoveRelativeDistance = lib.BDC_RequestMoveRelativeDistance
BDC_RequestMoveRelativeDistance.restype = c_short
BDC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


def request_move_relative_distance(serial_number, channel):
    # Requests the relative move distance.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestMoveRelativeDistance(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestPosition = lib.BDC_RequestPosition
BDC_RequestPosition.restype = c_short
BDC_RequestPosition.argtypes = [POINTER(c_char), c_short]


def request_position(serial_number, channel):
    # Requests the current position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestRackDigitalOutputs = lib.BDC_RequestRackDigitalOutputs
BDC_RequestRackDigitalOutputs.restype = c_short
BDC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


def request_rack_digital_outputs(serial_number):
    # Requests the rack digital output bits.

    serial_number = POINTER(c_char)

    output = BDC_RequestRackDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_RequestRackStatusBits = lib.BDC_RequestRackStatusBits
BDC_RequestRackStatusBits.restype = c_short
BDC_RequestRackStatusBits.argtypes = [POINTER(c_char)]


def request_rack_status_bits(serial_number):
    # Requests the Rack status bits be downloaded.

    serial_number = POINTER(c_char)

    output = BDC_RequestRackStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


BDC_RequestSettings = lib.BDC_RequestSettings
BDC_RequestSettings.restype = c_short
BDC_RequestSettings.argtypes = [POINTER(c_char), c_short]


def request_settings(serial_number, channel):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestSettings(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestStatusBits = lib.BDC_RequestStatusBits
BDC_RequestStatusBits.restype = c_short
BDC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]


def request_status_bits(serial_number, channel):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestTriggerConfigParams = lib.BDC_RequestTriggerConfigParams
BDC_RequestTriggerConfigParams.restype = c_short
BDC_RequestTriggerConfigParams.argtypes = [POINTER(c_char), c_short]


def request_trigger_config_params(serial_number, channel):
    # Requests the trigger parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestTriggerConfigParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestTriggerParams = lib.BDC_RequestTriggerParams
BDC_RequestTriggerParams.restype = c_short
BDC_RequestTriggerParams.argtypes = [POINTER(c_char), c_short]


def request_trigger_params(serial_number, channel):
    # Requests the trigger parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestTriggerParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestTriggerSwitches = lib.BDC_RequestTriggerSwitches
BDC_RequestTriggerSwitches.restype = c_short
BDC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]


def request_trigger_switches(serial_number, channel):
    # Requests the trigger switch parameter.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestTriggerSwitches(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_RequestVelParams = lib.BDC_RequestVelParams
BDC_RequestVelParams.restype = c_short
BDC_RequestVelParams.argtypes = [POINTER(c_char), c_short]


def request_vel_params(serial_number, channel):
    # Requests the velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_RequestVelParams(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_ResetRotationModes = lib.BDC_ResetRotationModes
BDC_ResetRotationModes.restype = c_short
BDC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]


def reset_rotation_modes(serial_number, channel):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_ResetRotationModes(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_ResumeMoveMessages = lib.BDC_ResumeMoveMessages
BDC_ResumeMoveMessages.restype = c_short
BDC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]


def resume_move_messages(serial_number, channel):
    # Resume suspended move messages.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_ResumeMoveMessages(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_SetBacklash = lib.BDC_SetBacklash
BDC_SetBacklash.restype = c_short
BDC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]


def set_backlash(serial_number, channel):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    channel = c_short()
    distance = c_long()

    output = BDC_SetBacklash(serial_number, channel, distance)
    if output != 0:
        raise KinesisException(output)


BDC_SetCalibrationFile = lib.BDC_SetCalibrationFile
BDC_SetCalibrationFile.restype = c_void_p
BDC_SetCalibrationFile.argtypes = [POINTER(c_char), c_short, POINTER(c_char), c_bool]


def set_calibration_file(serial_number, channel):
    # Set the calibration file for this motor.

    serial_number = POINTER(c_char)
    channel = c_short()
    filename = POINTER(c_char)
    enabled = c_bool()

    output = BDC_SetCalibrationFile(serial_number, channel, filename, enabled)
    if output != 0:
        raise KinesisException(output)


BDC_SetDCPIDParams = lib.BDC_SetDCPIDParams
BDC_SetDCPIDParams.restype = c_short
BDC_SetDCPIDParams.argtypes = [POINTER(c_char), MOT_DC_PIDParameters, c_short]


def set_d_c_p_i_d_params(serial_number, channel):
    # Sets the DC PID parameters.

    serial_number = POINTER(c_char)
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()
    channel = c_short()

    output = BDC_SetDCPIDParams(serial_number, DCproportionalIntegralDerivativeParams, channel)
    if output != 0:
        raise KinesisException(output)


BDC_SetDigitalOutputs = lib.BDC_SetDigitalOutputs
BDC_SetDigitalOutputs.restype = c_short
BDC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]


def set_digital_outputs(serial_number, channel):
    # Sets the digital output bits.

    serial_number = POINTER(c_char)
    channel = c_short()
    outputsBits = c_byte()

    output = BDC_SetDigitalOutputs(serial_number, channel, outputsBits)
    if output != 0:
        raise KinesisException(output)


BDC_SetDirection = lib.BDC_SetDirection
BDC_SetDirection.restype = c_short
BDC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]


def set_direction(serial_number, channel):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    channel = c_short()
    reverse = c_bool()

    output = BDC_SetDirection(serial_number, channel, reverse)
    if output != 0:
        raise KinesisException(output)


BDC_SetEncoderCounter = lib.BDC_SetEncoderCounter
BDC_SetEncoderCounter.restype = c_short
BDC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]


def set_encoder_counter(serial_number, channel):
    # Set the Encoder Counter values.

    serial_number = POINTER(c_char)
    channel = c_short()
    count = c_long()

    output = BDC_SetEncoderCounter(serial_number, channel, count)
    if output != 0:
        raise KinesisException(output)


BDC_SetHomingParamsBlock = lib.BDC_SetHomingParamsBlock
BDC_SetHomingParamsBlock.restype = c_short
BDC_SetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


def set_homing_params_block(serial_number, channel):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = BDC_SetHomingParamsBlock(serial_number, channel, homingParams)
    if output != 0:
        raise KinesisException(output)


BDC_SetHomingVelocity = lib.BDC_SetHomingVelocity
BDC_SetHomingVelocity.restype = c_short
BDC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]


def set_homing_velocity(serial_number, channel):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocity = c_uint()

    output = BDC_SetHomingVelocity(serial_number, channel, velocity)
    if output != 0:
        raise KinesisException(output)


BDC_SetJogMode = lib.BDC_SetJogMode
BDC_SetJogMode.restype = c_short
BDC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number, channel):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BDC_SetJogMode(serial_number, channel, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


BDC_SetJogParamsBlock = lib.BDC_SetJogParamsBlock
BDC_SetJogParamsBlock.restype = c_short
BDC_SetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters]


def set_jog_params_block(serial_number, channel):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    jogParams = MOT_JogParameters()

    output = BDC_SetJogParamsBlock(serial_number, channel, jogParams)
    if output != 0:
        raise KinesisException(output)


BDC_SetJogStepSize = lib.BDC_SetJogStepSize
BDC_SetJogStepSize.restype = c_short
BDC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]


def set_jog_step_size(serial_number, channel):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepSize = c_uint()

    output = BDC_SetJogStepSize(serial_number, channel, stepSize)
    if output != 0:
        raise KinesisException(output)


BDC_SetJogVelParams = lib.BDC_SetJogVelParams
BDC_SetJogVelParams.restype = c_short
BDC_SetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_jog_vel_params(serial_number, channel):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BDC_SetJogVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BDC_SetLimitSwitchParams = lib.BDC_SetLimitSwitchParams
BDC_SetLimitSwitchParams.restype = c_short
BDC_SetLimitSwitchParams.argtypes = [
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

    output = BDC_SetLimitSwitchParams(
        serial_number,
        channel,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


BDC_SetLimitSwitchParamsBlock = lib.BDC_SetLimitSwitchParamsBlock
BDC_SetLimitSwitchParamsBlock.restype = c_short
BDC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LimitSwitchParameters]


def set_limit_switch_params_block(serial_number, channel):
    # Set the limit switch parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = BDC_SetLimitSwitchParamsBlock(serial_number, channel, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


BDC_SetLimitsSoftwareApproachPolicy = lib.BDC_SetLimitsSoftwareApproachPolicy
BDC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
BDC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number, channel):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = BDC_SetLimitsSoftwareApproachPolicy(serial_number, channel, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


BDC_SetMotorParams = lib.BDC_SetMotorParams
BDC_SetMotorParams.restype = c_short
BDC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_float]


def set_motor_params(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = BDC_SetMotorParams(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BDC_SetMotorParamsExt = lib.BDC_SetMotorParamsExt
BDC_SetMotorParamsExt.restype = c_short
BDC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double, c_double, c_double]


def set_motor_params_ext(serial_number, channel):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = BDC_SetMotorParamsExt(serial_number, channel, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


BDC_SetMotorTravelLimits = lib.BDC_SetMotorTravelLimits
BDC_SetMotorTravelLimits.restype = c_short
BDC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def set_motor_travel_limits(serial_number, channel):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = BDC_SetMotorTravelLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BDC_SetMotorTravelMode = lib.BDC_SetMotorTravelMode
BDC_SetMotorTravelMode.restype = c_short
BDC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]


def set_motor_travel_mode(serial_number, channel):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    travelMode = MOT_TravelModes()

    output = BDC_SetMotorTravelMode(serial_number, channel, travelMode)
    if output != 0:
        raise KinesisException(output)


BDC_SetMotorVelocityLimits = lib.BDC_SetMotorVelocityLimits
BDC_SetMotorVelocityLimits.restype = c_short
BDC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


def set_motor_velocity_limits(serial_number, channel):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BDC_SetMotorVelocityLimits(serial_number, channel, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


BDC_SetMoveAbsolutePosition = lib.BDC_SetMoveAbsolutePosition
BDC_SetMoveAbsolutePosition.restype = c_short
BDC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]


def set_move_absolute_position(serial_number, channel):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    channel = c_short()
    position = c_int()

    output = BDC_SetMoveAbsolutePosition(serial_number, channel, position)
    if output != 0:
        raise KinesisException(output)


BDC_SetMoveRelativeDistance = lib.BDC_SetMoveRelativeDistance
BDC_SetMoveRelativeDistance.restype = c_short
BDC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]


def set_move_relative_distance(serial_number, channel):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    channel = c_short()
    distance = c_int()

    output = BDC_SetMoveRelativeDistance(serial_number, channel, distance)
    if output != 0:
        raise KinesisException(output)


BDC_SetPositionCounter = lib.BDC_SetPositionCounter
BDC_SetPositionCounter.restype = c_short
BDC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]


def set_position_counter(serial_number, channel):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    channel = c_short()
    count = c_long()

    output = BDC_SetPositionCounter(serial_number, channel, count)
    if output != 0:
        raise KinesisException(output)


BDC_SetRackDigitalOutputs = lib.BDC_SetRackDigitalOutputs
BDC_SetRackDigitalOutputs.restype = c_short
BDC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]


def set_rack_digital_outputs(serial_number):
    # Sets the rack digital output bits.

    serial_number = POINTER(c_char)
    outputsBits = c_byte()

    output = BDC_SetRackDigitalOutputs(serial_number, outputsBits)
    if output != 0:
        raise KinesisException(output)


BDC_SetRotationModes = lib.BDC_SetRotationModes
BDC_SetRotationModes.restype = c_short
BDC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number, channel):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = BDC_SetRotationModes(serial_number, channel, mode, direction)
    if output != 0:
        raise KinesisException(output)


BDC_SetStageAxisLimits = lib.BDC_SetStageAxisLimits
BDC_SetStageAxisLimits.restype = c_short
BDC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_stage_axis_limits(serial_number, channel):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    channel = c_short()
    minPosition = c_int()
    maxPosition = c_int()

    output = BDC_SetStageAxisLimits(serial_number, channel, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


BDC_SetTriggerConfigParams = lib.BDC_SetTriggerConfigParams
BDC_SetTriggerConfigParams.restype = c_short
BDC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    c_short,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity]


def set_trigger_config_params(serial_number, channel):
    # Sets the trigger configuration parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BDC_SetTriggerConfigParams(
        serial_number,
        channel,
        trigger1Mode,
        trigger1Polarity,
        trigger2Mode,
        trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


BDC_SetTriggerConfigParamsBlock = lib.BDC_SetTriggerConfigParamsBlock
BDC_SetTriggerConfigParamsBlock.restype = c_short
BDC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), c_short, KMOT_TriggerConfig]


def set_trigger_config_params_block(serial_number, channel):
    # Sets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    channel = c_short()
    triggerConfigParams = KMOT_TriggerConfig()

    output = BDC_SetTriggerConfigParamsBlock(serial_number, channel, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


BDC_SetTriggerParams = lib.BDC_SetTriggerParams
BDC_SetTriggerParams.restype = c_short
BDC_SetTriggerParams.argtypes = [
    POINTER(c_char),
    c_short,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32]


def set_trigger_params(serial_number, channel):
    # Sets the trigger parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BDC_SetTriggerParams(
        serial_number,
        channel,
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


BDC_SetTriggerParamsBlock = lib.BDC_SetTriggerParamsBlock
BDC_SetTriggerParamsBlock.restype = c_short
BDC_SetTriggerParamsBlock.argtypes = [POINTER(c_char), c_short, KMOT_TriggerParams]


def set_trigger_params_block(serial_number, channel):
    # Sets the trigger parameters block.

    serial_number = POINTER(c_char)
    channel = c_short()
    triggerParams = KMOT_TriggerParams()

    output = BDC_SetTriggerParamsBlock(serial_number, channel, triggerParams)
    if output != 0:
        raise KinesisException(output)


BDC_SetTriggerSwitches = lib.BDC_SetTriggerSwitches
BDC_SetTriggerSwitches.restype = c_short
BDC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]


def set_trigger_switches(serial_number, channel):
    # Sets the trigger switch parameter.

    serial_number = POINTER(c_char)
    channel = c_short()
    indicatorBits = c_byte()

    output = BDC_SetTriggerSwitches(serial_number, channel, indicatorBits)
    if output != 0:
        raise KinesisException(output)


BDC_SetVelParams = lib.BDC_SetVelParams
BDC_SetVelParams.restype = c_short
BDC_SetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


def set_vel_params(serial_number, channel):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BDC_SetVelParams(serial_number, channel, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


BDC_SetVelParamsBlock = lib.BDC_SetVelParamsBlock
BDC_SetVelParamsBlock.restype = c_short
BDC_SetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters]


def set_vel_params_block(serial_number, channel):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()

    output = BDC_SetVelParamsBlock(serial_number, channel, velocityParams)
    if output != 0:
        raise KinesisException(output)


BDC_StartPolling = lib.BDC_StartPolling
BDC_StartPolling.restype = c_bool
BDC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]


def start_polling(serial_number, channel):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    channel = c_short()
    milliseconds = c_int()

    output = BDC_StartPolling(serial_number, channel, milliseconds)

    return output


BDC_StopImmediate = lib.BDC_StopImmediate
BDC_StopImmediate.restype = c_short
BDC_StopImmediate.argtypes = [POINTER(c_char), c_short]


def stop_immediate(serial_number, channel):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_StopImmediate(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_StopPolling = lib.BDC_StopPolling
BDC_StopPolling.restype = c_void_p
BDC_StopPolling.argtypes = [POINTER(c_char), c_short]


def stop_polling(serial_number, channel):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_StopPolling(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_StopProfiled = lib.BDC_StopProfiled
BDC_StopProfiled.restype = c_short
BDC_StopProfiled.argtypes = [POINTER(c_char), c_short]


def stop_profiled(serial_number, channel):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_StopProfiled(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_SuspendMoveMessages = lib.BDC_SuspendMoveMessages
BDC_SuspendMoveMessages.restype = c_short
BDC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]


def suspend_move_messages(serial_number, channel):
    # Suspend automatic messages at ends of moves.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = BDC_SuspendMoveMessages(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


BDC_TimeSinceLastMsgReceived = lib.BDC_TimeSinceLastMsgReceived
BDC_TimeSinceLastMsgReceived.restype = c_bool
BDC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_short, c_int64]


def time_since_last_msg_received(serial_number, channel):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    channel = c_short()
    lastUpdateTimeMS = c_int64()

    output = BDC_TimeSinceLastMsgReceived(serial_number, channel, lastUpdateTimeMS)

    return output


BDC_WaitForMessage = lib.BDC_WaitForMessage
BDC_WaitForMessage.restype = c_bool
BDC_WaitForMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


def wait_for_message(serial_number, channel):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BDC_WaitForMessage(serial_number, channel, messageType, messageID, messageData)

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
