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
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_PowerParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.IntegratedStepperMotors.DLL")

ISC_CanHome = lib.ISC_CanHome
ISC_CanHome.restype = c_bool
ISC_CanHome.argtypes = [POINTER(c_char)]


def can_home(serial_number):
    # Can the device perform a Home.

    serial_number = POINTER(c_char)

    output = ISC_CanHome(serial_number)

    return output


ISC_CanMoveWithoutHomingFirst = lib.ISC_CanMoveWithoutHomingFirst
ISC_CanMoveWithoutHomingFirst.restype = c_bool
ISC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


def can_move_without_homing_first(serial_number):
    # Can this device be moved without Homing.

    serial_number = POINTER(c_char)

    output = ISC_CanMoveWithoutHomingFirst(serial_number)

    return output


ISC_CheckConnection = lib.ISC_CheckConnection
ISC_CheckConnection.restype = c_bool
ISC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = ISC_CheckConnection(serial_number)

    return output


ISC_ClearMessageQueue = lib.ISC_ClearMessageQueue
ISC_ClearMessageQueue.restype = c_void_p
ISC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = ISC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_Close = lib.ISC_Close
ISC_Close.restype = c_void_p
ISC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = ISC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_DisableChannel = lib.ISC_DisableChannel
ISC_DisableChannel.restype = c_short
ISC_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel(serial_number):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)

    output = ISC_DisableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_EnableChannel = lib.ISC_EnableChannel
ISC_EnableChannel.restype = c_short
ISC_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel(serial_number):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)

    output = ISC_EnableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_EnableLastMsgTimer = lib.ISC_EnableLastMsgTimer
ISC_EnableLastMsgTimer.restype = c_void_p
ISC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = ISC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


ISC_GetBacklash = lib.ISC_GetBacklash
ISC_GetBacklash.restype = c_long
ISC_GetBacklash.argtypes = [POINTER(c_char)]


def get_backlash(serial_number):
    # Get the backlash distance setting (used to control hysteresis).

    serial_number = POINTER(c_char)

    output = ISC_GetBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetBowIndex = lib.ISC_GetBowIndex
ISC_GetBowIndex.restype = c_short
ISC_GetBowIndex.argtypes = [POINTER(c_char)]


def get_bow_index(serial_number):
    # Gets the stepper motor bow index.

    serial_number = POINTER(c_char)

    output = ISC_GetBowIndex(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetButtonParams = lib.ISC_GetButtonParams
ISC_GetButtonParams.restype = c_short
ISC_GetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int, c_short]


def get_button_params(serial_number):
    # Gets the LTS button parameters.

    serial_number = POINTER(c_char)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()
    timeout = c_short()

    output = ISC_GetButtonParams(serial_number, buttonMode, leftButtonPosition, rightButtonPosition, timeout)
    if output != 0:
        raise KinesisException(output)


ISC_GetButtonParamsBlock = lib.ISC_GetButtonParamsBlock
ISC_GetButtonParamsBlock.restype = c_short
ISC_GetButtonParamsBlock.argtypes = [POINTER(c_char), MOT_ButtonParameters]


def get_button_params_block(serial_number):
    # Get the button parameters.

    serial_number = POINTER(c_char)
    buttonParams = MOT_ButtonParameters()

    output = ISC_GetButtonParamsBlock(serial_number, buttonParams)
    if output != 0:
        raise KinesisException(output)


ISC_GetCalibrationFile = lib.ISC_GetCalibrationFile
ISC_GetCalibrationFile.restype = c_bool
ISC_GetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_short]


def get_calibration_file(serial_number):
    # Get calibration file for this motor.

    serial_number = POINTER(c_char)
    filename = POINTER(c_char)
    sizeOfBuffer = c_short()

    output = ISC_GetCalibrationFile(serial_number, filename, sizeOfBuffer)

    return output


ISC_GetDeviceUnitFromRealValue = lib.ISC_GetDeviceUnitFromRealValue
ISC_GetDeviceUnitFromRealValue.restype = c_short
ISC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_double, c_int, c_int]


def get_device_unit_from_real_value(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = ISC_GetDeviceUnitFromRealValue(serial_number, real_unit, device_unit, unitType)
    if output != 0:
        raise KinesisException(output)


ISC_GetFirmwareVersion = lib.ISC_GetFirmwareVersion
ISC_GetFirmwareVersion.restype = c_ulong
ISC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = ISC_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetHardwareInfo = lib.ISC_GetHardwareInfo
ISC_GetHardwareInfo.restype = c_short
ISC_GetHardwareInfo.argtypes = [
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

    output = ISC_GetHardwareInfo(
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


ISC_GetHardwareInfoBlock = lib.ISC_GetHardwareInfoBlock
ISC_GetHardwareInfoBlock.restype = c_short
ISC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = ISC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


ISC_GetHomingParamsBlock = lib.ISC_GetHomingParamsBlock
ISC_GetHomingParamsBlock.restype = c_short
ISC_GetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def get_homing_params_block(serial_number):
    # Get the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = ISC_GetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


ISC_GetHomingVelocity = lib.ISC_GetHomingVelocity
ISC_GetHomingVelocity.restype = c_uint
ISC_GetHomingVelocity.argtypes = [POINTER(c_char)]


def get_homing_velocity(serial_number):
    # Gets the homing velocity.

    serial_number = POINTER(c_char)

    output = ISC_GetHomingVelocity(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetJogMode = lib.ISC_GetJogMode
ISC_GetJogMode.restype = c_short
ISC_GetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def get_jog_mode(serial_number):
    # Gets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = ISC_GetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


ISC_GetJogParamsBlock = lib.ISC_GetJogParamsBlock
ISC_GetJogParamsBlock.restype = c_short
ISC_GetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def get_jog_params_block(serial_number):
    # Get the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = ISC_GetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


ISC_GetJogStepSize = lib.ISC_GetJogStepSize
ISC_GetJogStepSize.restype = c_uint
ISC_GetJogStepSize.argtypes = [POINTER(c_char)]


def get_jog_step_size(serial_number):
    # Gets the distance to move when jogging.

    serial_number = POINTER(c_char)

    output = ISC_GetJogStepSize(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetJogVelParams = lib.ISC_GetJogVelParams
ISC_GetJogVelParams.restype = c_short
ISC_GetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_jog_vel_params(serial_number):
    # Gets the jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_GetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


ISC_GetLEDswitches = lib.ISC_GetLEDswitches
ISC_GetLEDswitches.restype = c_long
ISC_GetLEDswitches.argtypes = [POINTER(c_char)]


def get_l_e_dswitches(serial_number):
    # Get the LED indicator bits on device.

    serial_number = POINTER(c_char)

    output = ISC_GetLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetLimitSwitchParams = lib.ISC_GetLimitSwitchParams
ISC_GetLimitSwitchParams.restype = c_short
ISC_GetLimitSwitchParams.argtypes = [
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

    output = ISC_GetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


ISC_GetLimitSwitchParamsBlock = lib.ISC_GetLimitSwitchParamsBlock
ISC_GetLimitSwitchParamsBlock.restype = c_short
ISC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def get_limit_switch_params_block(serial_number):
    # Get the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = ISC_GetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


ISC_GetMotorParams = lib.ISC_GetMotorParams
ISC_GetMotorParams.restype = c_short
ISC_GetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def get_motor_params(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = ISC_GetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


ISC_GetMotorParamsExt = lib.ISC_GetMotorParamsExt
ISC_GetMotorParamsExt.restype = c_short
ISC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def get_motor_params_ext(serial_number):
    # Gets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = ISC_GetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


ISC_GetMotorTravelLimits = lib.ISC_GetMotorTravelLimits
ISC_GetMotorTravelLimits.restype = c_short
ISC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_travel_limits(serial_number):
    # Gets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = ISC_GetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


ISC_GetMotorTravelMode = lib.ISC_GetMotorTravelMode
ISC_GetMotorTravelMode.restype = MOT_TravelModes
ISC_GetMotorTravelMode.argtypes = [POINTER(c_char)]


def get_motor_travel_mode(serial_number):
    # Get the motor travel mode.

    serial_number = POINTER(c_char)

    output = ISC_GetMotorTravelMode(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetMotorVelocityLimits = lib.ISC_GetMotorVelocityLimits
ISC_GetMotorVelocityLimits.restype = c_short
ISC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def get_motor_velocity_limits(serial_number):
    # Gets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = ISC_GetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


ISC_GetMoveAbsolutePosition = lib.ISC_GetMoveAbsolutePosition
ISC_GetMoveAbsolutePosition.restype = c_int
ISC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def get_move_absolute_position(serial_number):
    # Gets the move absolute position.

    serial_number = POINTER(c_char)

    output = ISC_GetMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetMoveRelativeDistance = lib.ISC_GetMoveRelativeDistance
ISC_GetMoveRelativeDistance.restype = c_int
ISC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


def get_move_relative_distance(serial_number):
    # Gets the move relative distance.

    serial_number = POINTER(c_char)

    output = ISC_GetMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetNextMessage = lib.ISC_GetNextMessage
ISC_GetNextMessage.restype = c_bool
ISC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = ISC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


ISC_GetNumberPositions = lib.ISC_GetNumberPositions
ISC_GetNumberPositions.restype = c_int
ISC_GetNumberPositions.argtypes = [POINTER(c_char)]


def get_number_positions(serial_number):
    # Get number of positions.

    serial_number = POINTER(c_char)

    output = ISC_GetNumberPositions(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetPosition = lib.ISC_GetPosition
ISC_GetPosition.restype = c_int
ISC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)

    output = ISC_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetPositionCounter = lib.ISC_GetPositionCounter
ISC_GetPositionCounter.restype = c_long
ISC_GetPositionCounter.argtypes = [POINTER(c_char)]


def get_position_counter(serial_number):
    # Get the Position Counter.

    serial_number = POINTER(c_char)

    output = ISC_GetPositionCounter(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetPotentiometerParams = lib.ISC_GetPotentiometerParams
ISC_GetPotentiometerParams.restype = c_short
ISC_GetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]


def get_potentiometer_params(serial_number):
    # Gets the potentiometer parameters for the LTS.

    serial_number = POINTER(c_char)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = ISC_GetPotentiometerParams(serial_number, index, thresholdDeflection, velocity)
    if output != 0:
        raise KinesisException(output)


ISC_GetPotentiometerParamsBlock = lib.ISC_GetPotentiometerParamsBlock
ISC_GetPotentiometerParamsBlock.restype = c_short
ISC_GetPotentiometerParamsBlock.argtypes = [POINTER(c_char), MOT_PotentiometerSteps]


def get_potentiometer_params_block(serial_number):
    # Get the potentiometer parameters.

    serial_number = POINTER(c_char)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = ISC_GetPotentiometerParamsBlock(serial_number, potentiometerSteps)
    if output != 0:
        raise KinesisException(output)


ISC_GetPowerParams = lib.ISC_GetPowerParams
ISC_GetPowerParams.restype = c_short
ISC_GetPowerParams.argtypes = [POINTER(c_char), MOT_PowerParameters]


def get_power_params(serial_number):
    # Gets the power parameters for the stepper motor.

    serial_number = POINTER(c_char)
    powerParams = MOT_PowerParameters()

    output = ISC_GetPowerParams(serial_number, powerParams)
    if output != 0:
        raise KinesisException(output)


ISC_GetRealValueFromDeviceUnit = lib.ISC_GetRealValueFromDeviceUnit
ISC_GetRealValueFromDeviceUnit.restype = c_short
ISC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_int, c_double, c_int]


def get_real_value_from_device_unit(serial_number):
    # Converts a device unit to a real world unit.

    serial_number = POINTER(c_char)
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = ISC_GetRealValueFromDeviceUnit(serial_number, device_unit, real_unit, unitType)
    if output != 0:
        raise KinesisException(output)


ISC_GetSoftLimitMode = lib.ISC_GetSoftLimitMode
ISC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
ISC_GetSoftLimitMode.argtypes = [POINTER(c_char)]


def get_soft_limit_mode(serial_number):
    # Gets the software limits mode.

    serial_number = POINTER(c_char)

    output = ISC_GetSoftLimitMode(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetSoftwareVersion = lib.ISC_GetSoftwareVersion
ISC_GetSoftwareVersion.restype = c_ulong
ISC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = ISC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetStageAxisMaxPos = lib.ISC_GetStageAxisMaxPos
ISC_GetStageAxisMaxPos.restype = c_int
ISC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


def get_stage_axis_max_pos(serial_number):
    # Gets the LTS Motor maximum stage position.

    serial_number = POINTER(c_char)

    output = ISC_GetStageAxisMaxPos(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetStageAxisMinPos = lib.ISC_GetStageAxisMinPos
ISC_GetStageAxisMinPos.restype = c_int
ISC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


def get_stage_axis_min_pos(serial_number):
    # Gets the LTS Motor minimum stage position.

    serial_number = POINTER(c_char)

    output = ISC_GetStageAxisMinPos(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetStatusBits = lib.ISC_GetStatusBits
ISC_GetStatusBits.restype = c_ulong
ISC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = ISC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetTriggerSwitches = lib.ISC_GetTriggerSwitches
ISC_GetTriggerSwitches.restype = c_byte
ISC_GetTriggerSwitches.argtypes = [POINTER(c_char)]


def get_trigger_switches(serial_number):
    # Gets the trigger switch bits.

    serial_number = POINTER(c_char)

    output = ISC_GetTriggerSwitches(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_GetVelParams = lib.ISC_GetVelParams
ISC_GetVelParams.restype = c_short
ISC_GetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def get_vel_params(serial_number):
    # Gets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_GetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


ISC_GetVelParamsBlock = lib.ISC_GetVelParamsBlock
ISC_GetVelParamsBlock.restype = c_short
ISC_GetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def get_vel_params_block(serial_number):
    # Get the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = ISC_GetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


ISC_HasLastMsgTimerOverrun = lib.ISC_HasLastMsgTimerOverrun
ISC_HasLastMsgTimerOverrun.restype = c_bool
ISC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by ISC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = ISC_HasLastMsgTimerOverrun(serial_number)

    return output


ISC_Home = lib.ISC_Home
ISC_Home.restype = c_short
ISC_Home.argtypes = [POINTER(c_char)]


def home(serial_number):
    # Home the device.

    serial_number = POINTER(c_char)

    output = ISC_Home(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_Identify = lib.ISC_Identify
ISC_Identify.restype = c_void_p
ISC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = ISC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_IsCalibrationActive = lib.ISC_IsCalibrationActive
ISC_IsCalibrationActive.restype = c_bool
ISC_IsCalibrationActive.argtypes = [POINTER(c_char)]


def is_calibration_active(serial_number):
    # Is a calibration file active for this motor.

    serial_number = POINTER(c_char)

    output = ISC_IsCalibrationActive(serial_number)

    return output


ISC_LoadNamedSettings = lib.ISC_LoadNamedSettings
ISC_LoadNamedSettings.restype = c_bool
ISC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = ISC_LoadNamedSettings(serial_number, settingsName)

    return output


ISC_LoadSettings = lib.ISC_LoadSettings
ISC_LoadSettings.restype = c_bool
ISC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = ISC_LoadSettings(serial_number)

    return output


ISC_MessageQueueSize = lib.ISC_MessageQueueSize
ISC_MessageQueueSize.restype = c_int
ISC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = ISC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_MoveAbsolute = lib.ISC_MoveAbsolute
ISC_MoveAbsolute.restype = c_short
ISC_MoveAbsolute.argtypes = [POINTER(c_char)]


def move_absolute(serial_number):
    # Moves the device to the position defined in the SetMoveAbsolute command.

    serial_number = POINTER(c_char)

    output = ISC_MoveAbsolute(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_MoveAtVelocity = lib.ISC_MoveAtVelocity
ISC_MoveAtVelocity.restype = c_short
ISC_MoveAtVelocity.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_at_velocity(serial_number):
    # Start moving at the current velocity in the specified direction.

    serial_number = POINTER(c_char)
    direction = MOT_TravelDirection()

    output = ISC_MoveAtVelocity(serial_number, direction)
    if output != 0:
        raise KinesisException(output)


ISC_MoveJog = lib.ISC_MoveJog
ISC_MoveJog.restype = c_short
ISC_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_jog(serial_number):
    # Perform a jog.

    serial_number = POINTER(c_char)
    jogDirection = MOT_TravelDirection()

    output = ISC_MoveJog(serial_number, jogDirection)
    if output != 0:
        raise KinesisException(output)


ISC_MoveRelative = lib.ISC_MoveRelative
ISC_MoveRelative.restype = c_short
ISC_MoveRelative.argtypes = [POINTER(c_char), c_int]


def move_relative(serial_number):
    # Move the motor by a relative amount.

    serial_number = POINTER(c_char)
    displacement = c_int()

    output = ISC_MoveRelative(serial_number, displacement)
    if output != 0:
        raise KinesisException(output)


ISC_MoveRelativeDistance = lib.ISC_MoveRelativeDistance
ISC_MoveRelativeDistance.restype = c_short
ISC_MoveRelativeDistance.argtypes = [POINTER(c_char)]


def move_relative_distance(serial_number):
    # Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    serial_number = POINTER(c_char)

    output = ISC_MoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_MoveToPosition = lib.ISC_MoveToPosition
ISC_MoveToPosition.restype = c_short
ISC_MoveToPosition.argtypes = [POINTER(c_char), c_int]


def move_to_position(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    index = c_int()

    output = ISC_MoveToPosition(serial_number, index)
    if output != 0:
        raise KinesisException(output)


ISC_NeedsHoming = lib.ISC_NeedsHoming
ISC_NeedsHoming.restype = c_bool
ISC_NeedsHoming.argtypes = [POINTER(c_char)]


def needs_homing(serial_number):
    # Does the device need to be Homed before a move can be performed.

    serial_number = POINTER(c_char)

    output = ISC_NeedsHoming(serial_number)

    return output


ISC_Open = lib.ISC_Open
ISC_Open.restype = c_short
ISC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = ISC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_PersistSettings = lib.ISC_PersistSettings
ISC_PersistSettings.restype = c_bool
ISC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = ISC_PersistSettings(serial_number)

    return output


ISC_PollingDuration = lib.ISC_PollingDuration
ISC_PollingDuration.restype = c_long
ISC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = ISC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RegisterMessageCallback = lib.ISC_RegisterMessageCallback
ISC_RegisterMessageCallback.restype = c_void_p
ISC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = ISC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


ISC_RequestBacklash = lib.ISC_RequestBacklash
ISC_RequestBacklash.restype = c_short
ISC_RequestBacklash.argtypes = [POINTER(c_char)]


def request_backlash(serial_number):
    # Requests the backlash.

    serial_number = POINTER(c_char)

    output = ISC_RequestBacklash(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestBowIndex = lib.ISC_RequestBowIndex
ISC_RequestBowIndex.restype = c_short
ISC_RequestBowIndex.argtypes = [POINTER(c_char)]


def request_bow_index(serial_number):
    # Requests the stepper motor bow index.

    serial_number = POINTER(c_char)

    output = ISC_RequestBowIndex(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestButtonParams = lib.ISC_RequestButtonParams
ISC_RequestButtonParams.restype = c_short
ISC_RequestButtonParams.argtypes = [POINTER(c_char)]


def request_button_params(serial_number):
    # Requests the LTS button parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestButtonParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestHomingParams = lib.ISC_RequestHomingParams
ISC_RequestHomingParams.restype = c_short
ISC_RequestHomingParams.argtypes = [POINTER(c_char)]


def request_homing_params(serial_number):
    # Requests the homing parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestHomingParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestJogParams = lib.ISC_RequestJogParams
ISC_RequestJogParams.restype = c_short
ISC_RequestJogParams.argtypes = [POINTER(c_char)]


def request_jog_params(serial_number):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestJogParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestLimitSwitchParams = lib.ISC_RequestLimitSwitchParams
ISC_RequestLimitSwitchParams.restype = c_short
ISC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]


def request_limit_switch_params(serial_number):
    # Requests the limit switch parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestLimitSwitchParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestMoveAbsolutePosition = lib.ISC_RequestMoveAbsolutePosition
ISC_RequestMoveAbsolutePosition.restype = c_short
ISC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def request_move_absolute_position(serial_number):
    # Requests the position of next absolute move.

    serial_number = POINTER(c_char)

    output = ISC_RequestMoveAbsolutePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestMoveRelativeDistance = lib.ISC_RequestMoveRelativeDistance
ISC_RequestMoveRelativeDistance.restype = c_short
ISC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


def request_move_relative_distance(serial_number):
    # Requests the relative move distance.

    serial_number = POINTER(c_char)

    output = ISC_RequestMoveRelativeDistance(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestPosition = lib.ISC_RequestPosition
ISC_RequestPosition.restype = c_short
ISC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current position.

    serial_number = POINTER(c_char)

    output = ISC_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestPotentiometerParams = lib.ISC_RequestPotentiometerParams
ISC_RequestPotentiometerParams.restype = c_short
ISC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]


def request_potentiometer_params(serial_number):
    # Requests the potentiometer parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestPotentiometerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestPowerParams = lib.ISC_RequestPowerParams
ISC_RequestPowerParams.restype = c_short
ISC_RequestPowerParams.argtypes = [POINTER(c_char)]


def request_power_params(serial_number):
    # Requests the power parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestPowerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestSettings = lib.ISC_RequestSettings
ISC_RequestSettings.restype = c_short
ISC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = ISC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestStatus = lib.ISC_RequestStatus
ISC_RequestStatus.restype = c_short
ISC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Request position and status bits.

    serial_number = POINTER(c_char)

    output = ISC_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestStatusBits = lib.ISC_RequestStatusBits
ISC_RequestStatusBits.restype = c_short
ISC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current motor state.

    serial_number = POINTER(c_char)

    output = ISC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestTriggerSwitches = lib.ISC_RequestTriggerSwitches
ISC_RequestTriggerSwitches.restype = c_short
ISC_RequestTriggerSwitches.argtypes = [POINTER(c_char)]


def request_trigger_switches(serial_number):
    # Requests, gets or sets trigger switch bits for Cage Rotator only.

    serial_number = POINTER(c_char)

    output = ISC_RequestTriggerSwitches(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_RequestVelParams = lib.ISC_RequestVelParams
ISC_RequestVelParams.restype = c_short
ISC_RequestVelParams.argtypes = [POINTER(c_char)]


def request_vel_params(serial_number):
    # Requests the velocity parameters.

    serial_number = POINTER(c_char)

    output = ISC_RequestVelParams(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_ResetRotationModes = lib.ISC_ResetRotationModes
ISC_ResetRotationModes.restype = c_short
ISC_ResetRotationModes.argtypes = [POINTER(c_char)]


def reset_rotation_modes(serial_number):
    # Reset the rotation modes for a rotational device.

    serial_number = POINTER(c_char)

    output = ISC_ResetRotationModes(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_ResetStageToDefaults = lib.ISC_ResetStageToDefaults
ISC_ResetStageToDefaults.restype = c_short
ISC_ResetStageToDefaults.argtypes = [POINTER(c_char)]


def reset_stage_to_defaults(serial_number):
    # Reset the stage settings to defaults.

    serial_number = POINTER(c_char)

    output = ISC_ResetStageToDefaults(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_SetBacklash = lib.ISC_SetBacklash
ISC_SetBacklash.restype = c_short
ISC_SetBacklash.argtypes = [POINTER(c_char), c_long]


def set_backlash(serial_number):
    # Sets the backlash distance (used to control hysteresis).

    serial_number = POINTER(c_char)
    distance = c_long()

    output = ISC_SetBacklash(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


ISC_SetBowIndex = lib.ISC_SetBowIndex
ISC_SetBowIndex.restype = c_short
ISC_SetBowIndex.argtypes = [POINTER(c_char), c_short]


def set_bow_index(serial_number):
    # Sets the stepper motor bow index.

    serial_number = POINTER(c_char)
    bowIndex = c_short()

    output = ISC_SetBowIndex(serial_number, bowIndex)
    if output != 0:
        raise KinesisException(output)


ISC_SetButtonParams = lib.ISC_SetButtonParams
ISC_SetButtonParams.restype = c_short
ISC_SetButtonParams.argtypes = [POINTER(c_char), MOT_ButtonModes, c_int, c_int]


def set_button_params(serial_number):
    # Sets the LTS button parameters.

    serial_number = POINTER(c_char)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()

    output = ISC_SetButtonParams(serial_number, buttonMode, leftButtonPosition, rightButtonPosition)
    if output != 0:
        raise KinesisException(output)


ISC_SetButtonParamsBlock = lib.ISC_SetButtonParamsBlock
ISC_SetButtonParamsBlock.restype = c_short
ISC_SetButtonParamsBlock.argtypes = [POINTER(c_char), MOT_ButtonParameters]


def set_button_params_block(serial_number):
    # Set the button parameters.

    serial_number = POINTER(c_char)
    buttonParams = MOT_ButtonParameters()

    output = ISC_SetButtonParamsBlock(serial_number, buttonParams)
    if output != 0:
        raise KinesisException(output)


ISC_SetCalibrationFile = lib.ISC_SetCalibrationFile
ISC_SetCalibrationFile.restype = c_void_p
ISC_SetCalibrationFile.argtypes = [POINTER(c_char), POINTER(c_char), c_bool]


def set_calibration_file(serial_number):
    # Set the calibration file for this motor.

    serial_number = POINTER(c_char)
    filename = POINTER(c_char)
    enabled = c_bool()

    output = ISC_SetCalibrationFile(serial_number, filename, enabled)
    if output != 0:
        raise KinesisException(output)


ISC_SetDirection = lib.ISC_SetDirection
ISC_SetDirection.restype = c_void_p
ISC_SetDirection.argtypes = [POINTER(c_char), c_bool]


def set_direction(serial_number):
    # Sets the motor direction sense.

    serial_number = POINTER(c_char)
    reverse = c_bool()

    output = ISC_SetDirection(serial_number, reverse)
    if output != 0:
        raise KinesisException(output)


ISC_SetHomingParamsBlock = lib.ISC_SetHomingParamsBlock
ISC_SetHomingParamsBlock.restype = c_short
ISC_SetHomingParamsBlock.argtypes = [POINTER(c_char), MOT_HomingParameters]


def set_homing_params_block(serial_number):
    # Set the homing parameters.

    serial_number = POINTER(c_char)
    homingParams = MOT_HomingParameters()

    output = ISC_SetHomingParamsBlock(serial_number, homingParams)
    if output != 0:
        raise KinesisException(output)


ISC_SetHomingVelocity = lib.ISC_SetHomingVelocity
ISC_SetHomingVelocity.restype = c_short
ISC_SetHomingVelocity.argtypes = [POINTER(c_char), c_uint]


def set_homing_velocity(serial_number):
    # Sets the homing velocity.

    serial_number = POINTER(c_char)
    velocity = c_uint()

    output = ISC_SetHomingVelocity(serial_number, velocity)
    if output != 0:
        raise KinesisException(output)


ISC_SetJogMode = lib.ISC_SetJogMode
ISC_SetJogMode.restype = c_short
ISC_SetJogMode.argtypes = [POINTER(c_char), MOT_JogModes, MOT_StopModes]


def set_jog_mode(serial_number):
    # Sets the jog mode.

    serial_number = POINTER(c_char)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = ISC_SetJogMode(serial_number, mode, stopMode)
    if output != 0:
        raise KinesisException(output)


ISC_SetJogParamsBlock = lib.ISC_SetJogParamsBlock
ISC_SetJogParamsBlock.restype = c_short
ISC_SetJogParamsBlock.argtypes = [POINTER(c_char), MOT_JogParameters]


def set_jog_params_block(serial_number):
    # Set the jog parameters.

    serial_number = POINTER(c_char)
    jogParams = MOT_JogParameters()

    output = ISC_SetJogParamsBlock(serial_number, jogParams)
    if output != 0:
        raise KinesisException(output)


ISC_SetJogStepSize = lib.ISC_SetJogStepSize
ISC_SetJogStepSize.restype = c_short
ISC_SetJogStepSize.argtypes = [POINTER(c_char), c_uint]


def set_jog_step_size(serial_number):
    # Sets the distance to move on jogging.

    serial_number = POINTER(c_char)
    stepSize = c_uint()

    output = ISC_SetJogStepSize(serial_number, stepSize)
    if output != 0:
        raise KinesisException(output)


ISC_SetJogVelParams = lib.ISC_SetJogVelParams
ISC_SetJogVelParams.restype = c_short
ISC_SetJogVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_jog_vel_params(serial_number):
    # Sets jog velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_SetJogVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


ISC_SetLEDswitches = lib.ISC_SetLEDswitches
ISC_SetLEDswitches.restype = c_short
ISC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]


def set_l_e_dswitches(serial_number):
    # Set the LED indicator bits on device.

    serial_number = POINTER(c_char)
    LEDswitches = c_long()

    output = ISC_SetLEDswitches(serial_number, LEDswitches)
    if output != 0:
        raise KinesisException(output)


ISC_SetLimitSwitchParams = lib.ISC_SetLimitSwitchParams
ISC_SetLimitSwitchParams.restype = c_short
ISC_SetLimitSwitchParams.argtypes = [
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

    output = ISC_SetLimitSwitchParams(
        serial_number,
        clockwiseHardwareLimit,
        anticlockwiseHardwareLimit,
        clockwisePosition,
        anticlockwisePosition,
        softLimitMode)
    if output != 0:
        raise KinesisException(output)


ISC_SetLimitSwitchParamsBlock = lib.ISC_SetLimitSwitchParamsBlock
ISC_SetLimitSwitchParamsBlock.restype = c_short
ISC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char), MOT_LimitSwitchParameters]


def set_limit_switch_params_block(serial_number):
    # Set the limit switch parameters.

    serial_number = POINTER(c_char)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = ISC_SetLimitSwitchParamsBlock(serial_number, limitSwitchParams)
    if output != 0:
        raise KinesisException(output)


ISC_SetLimitsSoftwareApproachPolicy = lib.ISC_SetLimitsSoftwareApproachPolicy
ISC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
ISC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), MOT_LimitsSoftwareApproachPolicy]


def set_limits_software_approach_policy(serial_number):
    # Sets the software limits mode.

    serial_number = POINTER(c_char)
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = ISC_SetLimitsSoftwareApproachPolicy(serial_number, limitsSoftwareApproachPolicy)
    if output != 0:
        raise KinesisException(output)


ISC_SetMotorParams = lib.ISC_SetMotorParams
ISC_SetMotorParams.restype = c_short
ISC_SetMotorParams.argtypes = [POINTER(c_char), c_long, c_long, c_float]


def set_motor_params(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = ISC_SetMotorParams(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


ISC_SetMotorParamsExt = lib.ISC_SetMotorParamsExt
ISC_SetMotorParamsExt.restype = c_short
ISC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_double, c_double, c_double]


def set_motor_params_ext(serial_number):
    # Sets the motor stage parameters.

    serial_number = POINTER(c_char)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = ISC_SetMotorParamsExt(serial_number, stepsPerRev, gearBoxRatio, pitch)
    if output != 0:
        raise KinesisException(output)


ISC_SetMotorTravelLimits = lib.ISC_SetMotorTravelLimits
ISC_SetMotorTravelLimits.restype = c_short
ISC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_travel_limits(serial_number):
    # Sets the absolute minimum and maximum travel range constants for the current stage.

    serial_number = POINTER(c_char)
    minPosition = c_double()
    maxPosition = c_double()

    output = ISC_SetMotorTravelLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


ISC_SetMotorTravelMode = lib.ISC_SetMotorTravelMode
ISC_SetMotorTravelMode.restype = c_short
ISC_SetMotorTravelMode.argtypes = [POINTER(c_char), MOT_TravelModes]


def set_motor_travel_mode(serial_number):
    # Set the motor travel mode.

    serial_number = POINTER(c_char)
    travelMode = MOT_TravelModes()

    output = ISC_SetMotorTravelMode(serial_number, travelMode)
    if output != 0:
        raise KinesisException(output)


ISC_SetMotorVelocityLimits = lib.ISC_SetMotorVelocityLimits
ISC_SetMotorVelocityLimits.restype = c_short
ISC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_double, c_double]


def set_motor_velocity_limits(serial_number):
    # Sets the absolute maximum velocity and acceleration constants for the current stage.

    serial_number = POINTER(c_char)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = ISC_SetMotorVelocityLimits(serial_number, maxVelocity, maxAcceleration)
    if output != 0:
        raise KinesisException(output)


ISC_SetMoveAbsolutePosition = lib.ISC_SetMoveAbsolutePosition
ISC_SetMoveAbsolutePosition.restype = c_short
ISC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_int]


def set_move_absolute_position(serial_number):
    # Sets the move absolute position.

    serial_number = POINTER(c_char)
    position = c_int()

    output = ISC_SetMoveAbsolutePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


ISC_SetMoveRelativeDistance = lib.ISC_SetMoveRelativeDistance
ISC_SetMoveRelativeDistance.restype = c_short
ISC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_int]


def set_move_relative_distance(serial_number):
    # Sets the move relative distance.

    serial_number = POINTER(c_char)
    distance = c_int()

    output = ISC_SetMoveRelativeDistance(serial_number, distance)
    if output != 0:
        raise KinesisException(output)


ISC_SetPositionCounter = lib.ISC_SetPositionCounter
ISC_SetPositionCounter.restype = c_short
ISC_SetPositionCounter.argtypes = [POINTER(c_char), c_long]


def set_position_counter(serial_number):
    # Set the Position Counter.

    serial_number = POINTER(c_char)
    count = c_long()

    output = ISC_SetPositionCounter(serial_number, count)
    if output != 0:
        raise KinesisException(output)


ISC_SetPotentiometerParams = lib.ISC_SetPotentiometerParams
ISC_SetPotentiometerParams.restype = c_short
ISC_SetPotentiometerParams.argtypes = [POINTER(c_char), c_short, c_long, c_ulong]


def set_potentiometer_params(serial_number):
    # Sets the potentiometer parameters for the LTS.

    serial_number = POINTER(c_char)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = ISC_SetPotentiometerParams(serial_number, index, thresholdDeflection, velocity)
    if output != 0:
        raise KinesisException(output)


ISC_SetPotentiometerParamsBlock = lib.ISC_SetPotentiometerParamsBlock
ISC_SetPotentiometerParamsBlock.restype = c_short
ISC_SetPotentiometerParamsBlock.argtypes = [POINTER(c_char), MOT_PotentiometerSteps]


def set_potentiometer_params_block(serial_number):
    # Set the potentiometer parameters.

    serial_number = POINTER(c_char)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = ISC_SetPotentiometerParamsBlock(serial_number, potentiometerSteps)
    if output != 0:
        raise KinesisException(output)


ISC_SetPowerParams = lib.ISC_SetPowerParams
ISC_SetPowerParams.restype = c_short
ISC_SetPowerParams.argtypes = [POINTER(c_char), MOT_PowerParameters]


def set_power_params(serial_number):
    # Sets the power parameters for the stepper motor.

    serial_number = POINTER(c_char)
    powerParams = MOT_PowerParameters()

    output = ISC_SetPowerParams(serial_number, powerParams)
    if output != 0:
        raise KinesisException(output)


ISC_SetRotationModes = lib.ISC_SetRotationModes
ISC_SetRotationModes.restype = c_short
ISC_SetRotationModes.argtypes = [POINTER(c_char), MOT_MovementModes, MOT_MovementDirections]


def set_rotation_modes(serial_number):
    # Set the rotation modes for a rotational device.

    serial_number = POINTER(c_char)
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = ISC_SetRotationModes(serial_number, mode, direction)
    if output != 0:
        raise KinesisException(output)


ISC_SetStageAxisLimits = lib.ISC_SetStageAxisLimits
ISC_SetStageAxisLimits.restype = c_short
ISC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_int, c_int]


def set_stage_axis_limits(serial_number):
    # Sets the stage axis position limits.

    serial_number = POINTER(c_char)
    minPosition = c_int()
    maxPosition = c_int()

    output = ISC_SetStageAxisLimits(serial_number, minPosition, maxPosition)
    if output != 0:
        raise KinesisException(output)


ISC_SetTriggerSwitches = lib.ISC_SetTriggerSwitches
ISC_SetTriggerSwitches.restype = c_short
ISC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_byte]


def set_trigger_switches(serial_number):
    # Sets the trigger switch bits.

    serial_number = POINTER(c_char)
    indicatorBits = c_byte()

    output = ISC_SetTriggerSwitches(serial_number, indicatorBits)
    if output != 0:
        raise KinesisException(output)


ISC_SetVelParams = lib.ISC_SetVelParams
ISC_SetVelParams.restype = c_short
ISC_SetVelParams.argtypes = [POINTER(c_char), c_int, c_int]


def set_vel_params(serial_number):
    # Sets the move velocity parameters.

    serial_number = POINTER(c_char)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_SetVelParams(serial_number, acceleration, maxVelocity)
    if output != 0:
        raise KinesisException(output)


ISC_SetVelParamsBlock = lib.ISC_SetVelParamsBlock
ISC_SetVelParamsBlock.restype = c_short
ISC_SetVelParamsBlock.argtypes = [POINTER(c_char), MOT_VelocityParameters]


def set_vel_params_block(serial_number):
    # Set the move velocity parameters.

    serial_number = POINTER(c_char)
    velocityParams = MOT_VelocityParameters()

    output = ISC_SetVelParamsBlock(serial_number, velocityParams)
    if output != 0:
        raise KinesisException(output)


ISC_StartPolling = lib.ISC_StartPolling
ISC_StartPolling.restype = c_bool
ISC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = ISC_StartPolling(serial_number, milliseconds)

    return output


ISC_StopImmediate = lib.ISC_StopImmediate
ISC_StopImmediate.restype = c_short
ISC_StopImmediate.argtypes = [POINTER(c_char)]


def stop_immediate(serial_number):
    # Stop the current move immediately (with risk of losing track of position).

    serial_number = POINTER(c_char)

    output = ISC_StopImmediate(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_StopPolling = lib.ISC_StopPolling
ISC_StopPolling.restype = c_void_p
ISC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = ISC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_StopProfiled = lib.ISC_StopProfiled
ISC_StopProfiled.restype = c_short
ISC_StopProfiled.argtypes = [POINTER(c_char)]


def stop_profiled(serial_number):
    # Stop the current move using the current velocity profile.

    serial_number = POINTER(c_char)

    output = ISC_StopProfiled(serial_number)
    if output != 0:
        raise KinesisException(output)


ISC_TimeSinceLastMsgReceived = lib.ISC_TimeSinceLastMsgReceived
ISC_TimeSinceLastMsgReceived.restype = c_bool
ISC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = ISC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


ISC_WaitForMessage = lib.ISC_WaitForMessage
ISC_WaitForMessage.restype = c_bool
ISC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = ISC_WaitForMessage(serial_number, messageType, messageID, messageData)

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
