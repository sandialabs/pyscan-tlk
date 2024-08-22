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
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
from .definitions.safearray import SafeArray
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
    lib_path + "Thorlabs.MotionControl.Benchtop.StepperMotor.dll")

SBC_CanHome = lib.SBC_CanHome
SBC_CanHome.restype = c_bool
SBC_CanHome.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_CanHome(serial_number)

    return output


SBC_CanMoveWithoutHomingFirst = lib.SBC_CanMoveWithoutHomingFirst
SBC_CanMoveWithoutHomingFirst.restype = c_bool
SBC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_CanMoveWithoutHomingFirst(serial_number)

    return output


SBC_CheckConnection = lib.SBC_CheckConnection
SBC_CheckConnection.restype = c_bool
SBC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    '''
    Check connection.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_CheckConnection(serial_number)

    return output


SBC_ClearMessageQueue = lib.SBC_ClearMessageQueue
SBC_ClearMessageQueue.restype = c_short
SBC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_ClearMessageQueue(serial_number)

    return output


SBC_Close = lib.SBC_Close
SBC_Close.restype = c_short
SBC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    '''
    Disconnect and close the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_Close(serial_number)

    return output


SBC_DisableChannel = lib.SBC_DisableChannel
SBC_DisableChannel.restype = c_short
SBC_DisableChannel.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_DisableChannel(serial_number)

    return output


SBC_EnableChannel = lib.SBC_EnableChannel
SBC_EnableChannel.restype = c_short
SBC_EnableChannel.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_EnableChannel(serial_number)

    return output


SBC_EnableLastMsgTimer = lib.SBC_EnableLastMsgTimer
SBC_EnableLastMsgTimer.restype = c_void_p
SBC_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SBC_EnableLastMsgTimer(serial_number)

    return output


SBC_GetBacklash = lib.SBC_GetBacklash
SBC_GetBacklash.restype = c_long
SBC_GetBacklash.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetBacklash(serial_number)

    return output


SBC_GetBowIndex = lib.SBC_GetBowIndex
SBC_GetBowIndex.restype = c_short
SBC_GetBowIndex.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetBowIndex(serial_number)

    return output


SBC_GetCalibrationFile = lib.SBC_GetCalibrationFile
SBC_GetCalibrationFile.restype = c_bool
SBC_GetCalibrationFile.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    filename = POINTER(c_char)()
    sizeOfBuffer = c_short()

    output = SBC_GetCalibrationFile(serial_number)

    return output


SBC_GetDeviceUnitFromRealValue = lib.SBC_GetDeviceUnitFromRealValue
SBC_GetDeviceUnitFromRealValue.restype = c_short
SBC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = SBC_GetDeviceUnitFromRealValue(serial_number)

    return output


SBC_GetDigitalOutputs = lib.SBC_GetDigitalOutputs
SBC_GetDigitalOutputs.restype = c_byte
SBC_GetDigitalOutputs.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetDigitalOutputs(serial_number)

    return output


SBC_GetEncoderCounter = lib.SBC_GetEncoderCounter
SBC_GetEncoderCounter.restype = c_long
SBC_GetEncoderCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetEncoderCounter(serial_number)

    return output


SBC_GetFirmwareVersion = lib.SBC_GetFirmwareVersion
SBC_GetFirmwareVersion.restype = c_ulong
SBC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    '''
    Gets version number of the device firmware.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetFirmwareVersion(serial_number)

    return output


SBC_GetHardwareInfo = lib.SBC_GetHardwareInfo
SBC_GetHardwareInfo.restype = c_short
SBC_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        modelNo: POINTER(c_char)
        sizeOfModelNo: c_ulong
        type: c_long
        numChannels: c_long
        notes: POINTER(c_char)
        sizeOfNotes: c_ulong
        firmwareVersion: c_ulong
        hardwareVersion: c_long
        modificationState: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = SBC_GetHardwareInfo(serial_number)

    return output


SBC_GetHardwareInfoBlock = lib.SBC_GetHardwareInfoBlock
SBC_GetHardwareInfoBlock.restype = c_short
SBC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        hardwareInfo: TLI_HardwareInformation

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    hardwareInfo = TLI_HardwareInformation()

    output = SBC_GetHardwareInfoBlock(serial_number)

    return output


SBC_GetHomingParamsBlock = lib.SBC_GetHomingParamsBlock
SBC_GetHomingParamsBlock.restype = c_short
SBC_GetHomingParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = SBC_GetHomingParamsBlock(serial_number)

    return output


SBC_GetHomingVelocity = lib.SBC_GetHomingVelocity
SBC_GetHomingVelocity.restype = c_uint
SBC_GetHomingVelocity.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetHomingVelocity(serial_number)

    return output


SBC_GetInputVoltage = lib.SBC_GetInputVoltage
SBC_GetInputVoltage.restype = c_long
SBC_GetInputVoltage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetInputVoltage(serial_number)

    return output


SBC_GetJogMode = lib.SBC_GetJogMode
SBC_GetJogMode.restype = c_short
SBC_GetJogMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SBC_GetJogMode(serial_number)

    return output


SBC_GetJogParamsBlock = lib.SBC_GetJogParamsBlock
SBC_GetJogParamsBlock.restype = c_short
SBC_GetJogParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    jogParams = MOT_JogParameters()
    jogParameters = MOT_JogParameters()

    output = SBC_GetJogParamsBlock(serial_number)

    return output


SBC_GetJogStepSize = lib.SBC_GetJogStepSize
SBC_GetJogStepSize.restype = c_uint
SBC_GetJogStepSize.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetJogStepSize(serial_number)

    return output


SBC_GetJogVelParams = lib.SBC_GetJogVelParams
SBC_GetJogVelParams.restype = c_short
SBC_GetJogVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_GetJogVelParams(serial_number)

    return output


SBC_GetJoystickParams = lib.SBC_GetJoystickParams
SBC_GetJoystickParams.restype = c_short
SBC_GetJoystickParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    joystickParams = MOT_JoystickParameters()

    output = SBC_GetJoystickParams(serial_number)

    return output


SBC_GetLimitSwitchParams = lib.SBC_GetLimitSwitchParams
SBC_GetLimitSwitchParams.restype = c_short
SBC_GetLimitSwitchParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
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
SBC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SBC_GetLimitSwitchParamsBlock(serial_number)

    return output


SBC_GetMotorParams = lib.SBC_GetMotorParams
SBC_GetMotorParams.restype = c_short
SBC_GetMotorParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SBC_GetMotorParams(serial_number)

    return output


SBC_GetMotorParamsExt = lib.SBC_GetMotorParamsExt
SBC_GetMotorParamsExt.restype = c_short
SBC_GetMotorParamsExt.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SBC_GetMotorParamsExt(serial_number)

    return output


SBC_GetMotorTravelLimits = lib.SBC_GetMotorTravelLimits
SBC_GetMotorTravelLimits.restype = c_short
SBC_GetMotorTravelLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = SBC_GetMotorTravelLimits(serial_number)

    return output


SBC_GetMotorTravelMode = lib.SBC_GetMotorTravelMode
SBC_GetMotorTravelMode.restype = MOT_TravelModes
SBC_GetMotorTravelMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetMotorTravelMode(serial_number)

    return output


SBC_GetMotorVelocityLimits = lib.SBC_GetMotorVelocityLimits
SBC_GetMotorVelocityLimits.restype = c_short
SBC_GetMotorVelocityLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SBC_GetMotorVelocityLimits(serial_number)

    return output


SBC_GetMoveAbsolutePosition = lib.SBC_GetMoveAbsolutePosition
SBC_GetMoveAbsolutePosition.restype = c_int
SBC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetMoveAbsolutePosition(serial_number)

    return output


SBC_GetMoveRelativeDistance = lib.SBC_GetMoveRelativeDistance
SBC_GetMoveRelativeDistance.restype = c_int
SBC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetMoveRelativeDistance(serial_number)

    return output


SBC_GetNextMessage = lib.SBC_GetNextMessage
SBC_GetNextMessage.restype = c_bool
SBC_GetNextMessage.argtypes = [POINTER(c_char)]


def get_next_message(serial_number):
    '''
    Get the next MessageQueue item if it is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SBC_GetNextMessage(serial_number)

    return output


SBC_GetNumChannels = lib.SBC_GetNumChannels
SBC_GetNumChannels.restype = c_short
SBC_GetNumChannels.argtypes = [POINTER(c_char)]


def get_num_channels(serial_number):
    '''
    Gets the number of channels in the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_GetNumChannels(serial_number)

    return output


SBC_GetNumberPositions = lib.SBC_GetNumberPositions
SBC_GetNumberPositions.restype = c_int
SBC_GetNumberPositions.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetNumberPositions(serial_number)

    return output


SBC_GetPIDLoopEncoderCoeff = lib.SBC_GetPIDLoopEncoderCoeff
SBC_GetPIDLoopEncoderCoeff.restype = c_double
SBC_GetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char)]


def get_p_i_d_loop_encoder_coeff(serial_number):
    '''
    Gets the Encoder PID loop encoder coefficient.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_double
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetPIDLoopEncoderCoeff(serial_number)

    return output


SBC_GetPIDLoopEncoderParams = lib.SBC_GetPIDLoopEncoderParams
SBC_GetPIDLoopEncoderParams.restype = c_short
SBC_GetPIDLoopEncoderParams.argtypes = [POINTER(c_char)]


def get_p_i_d_loop_encoder_params(serial_number):
    '''
    Gets the Encoder PID loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        params: MOT_PIDLoopEncoderParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    params = MOT_PIDLoopEncoderParams()

    output = SBC_GetPIDLoopEncoderParams(serial_number)

    return output


SBC_GetPosition = lib.SBC_GetPosition
SBC_GetPosition.restype = c_int
SBC_GetPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetPosition(serial_number)

    return output


SBC_GetPositionCounter = lib.SBC_GetPositionCounter
SBC_GetPositionCounter.restype = c_long
SBC_GetPositionCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetPositionCounter(serial_number)

    return output


SBC_GetPowerParams = lib.SBC_GetPowerParams
SBC_GetPowerParams.restype = c_short
SBC_GetPowerParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    powerParams = MOT_PowerParameters()

    output = SBC_GetPowerParams(serial_number)

    return output


SBC_GetRackDigitalOutputs = lib.SBC_GetRackDigitalOutputs
SBC_GetRackDigitalOutputs.restype = c_byte
SBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def get_rack_digital_outputs(serial_number):
    '''
    Gets the rack digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_GetRackDigitalOutputs(serial_number)

    return output


SBC_GetRackStatusBits = lib.SBC_GetRackStatusBits
SBC_GetRackStatusBits.restype = c_ulong
SBC_GetRackStatusBits.argtypes = [POINTER(c_char)]


def get_rack_status_bits(serial_number):
    '''
    Gets the Rack status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_GetRackStatusBits(serial_number)

    return output


SBC_GetRealValueFromDeviceUnit = lib.SBC_GetRealValueFromDeviceUnit
SBC_GetRealValueFromDeviceUnit.restype = c_short
SBC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = SBC_GetRealValueFromDeviceUnit(serial_number)

    return output


SBC_GetSoftLimitMode = lib.SBC_GetSoftLimitMode
SBC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SBC_GetSoftLimitMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetSoftLimitMode(serial_number)

    return output


SBC_GetSoftwareVersion = lib.SBC_GetSoftwareVersion
SBC_GetSoftwareVersion.restype = c_ulong
SBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    '''
    Gets version number of the device software.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_GetSoftwareVersion(serial_number)

    return output


SBC_GetStageAxisMaxPos = lib.SBC_GetStageAxisMaxPos
SBC_GetStageAxisMaxPos.restype = c_int
SBC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetStageAxisMaxPos(serial_number)

    return output


SBC_GetStageAxisMinPos = lib.SBC_GetStageAxisMinPos
SBC_GetStageAxisMinPos.restype = c_int
SBC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetStageAxisMinPos(serial_number)

    return output


SBC_GetStatusBits = lib.SBC_GetStatusBits
SBC_GetStatusBits.restype = c_ulong
SBC_GetStatusBits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetStatusBits(serial_number)

    return output


SBC_GetTriggerSwitches = lib.SBC_GetTriggerSwitches
SBC_GetTriggerSwitches.restype = c_byte
SBC_GetTriggerSwitches.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_GetTriggerSwitches(serial_number)

    return output


SBC_GetVelParams = lib.SBC_GetVelParams
SBC_GetVelParams.restype = c_short
SBC_GetVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_GetVelParams(serial_number)

    return output


SBC_GetVelParamsBlock = lib.SBC_GetVelParamsBlock
SBC_GetVelParamsBlock.restype = c_short
SBC_GetVelParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    velocityParams = MOT_VelocityParameters()
    velocityParameters = MOT_VelocityParameters()

    output = SBC_GetVelParamsBlock(serial_number)

    return output


SBC_HasLastMsgTimerOverrun = lib.SBC_HasLastMsgTimerOverrun
SBC_HasLastMsgTimerOverrun.restype = c_bool
SBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_HasLastMsgTimerOverrun(serial_number)

    return output


SBC_Home = lib.SBC_Home
SBC_Home.restype = c_short
SBC_Home.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_Home(serial_number)

    return output


SBC_Identify = lib.SBC_Identify
SBC_Identify.restype = c_void_p
SBC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    '''
    Sends a command to the device to make it identify iteself.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_Identify(serial_number)

    return output


SBC_IsCalibrationActive = lib.SBC_IsCalibrationActive
SBC_IsCalibrationActive.restype = c_bool
SBC_IsCalibrationActive.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_IsCalibrationActive(serial_number)

    return output


SBC_IsChannelValid = lib.SBC_IsChannelValid
SBC_IsChannelValid.restype = c_bool
SBC_IsChannelValid.argtypes = [POINTER(c_char)]


def is_channel_valid(serial_number):
    '''
    Verifies that the specified channel is valid.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_IsChannelValid(serial_number)

    return output


SBC_LoadNamedSettings = lib.SBC_LoadNamedSettings
SBC_LoadNamedSettings.restype = c_bool
SBC_LoadNamedSettings.argtypes = [POINTER(c_char)]


def load_named_settings(serial_number):
    '''
    Update device with named settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        settingsName: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    settingsName = POINTER(c_char)()

    output = SBC_LoadNamedSettings(serial_number)

    return output


SBC_LoadSettings = lib.SBC_LoadSettings
SBC_LoadSettings.restype = c_bool
SBC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_LoadSettings(serial_number)

    return output


SBC_MaxChannelCount = lib.SBC_MaxChannelCount
SBC_MaxChannelCount.restype = c_int
SBC_MaxChannelCount.argtypes = [POINTER(c_char)]


def max_channel_count(serial_number):
    '''
    Gets the number of channels available to this device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_MaxChannelCount(serial_number)

    return output


SBC_MessageQueueSize = lib.SBC_MessageQueueSize
SBC_MessageQueueSize.restype = c_int
SBC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    '''
    Gets the MessageQueue size.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_MessageQueueSize(serial_number)

    return output


SBC_MoveAbsolute = lib.SBC_MoveAbsolute
SBC_MoveAbsolute.restype = c_short
SBC_MoveAbsolute.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_MoveAbsolute(serial_number)

    return output


SBC_MoveAtVelocity = lib.SBC_MoveAtVelocity
SBC_MoveAtVelocity.restype = c_short
SBC_MoveAtVelocity.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    direction = MOT_TravelDirection()

    output = SBC_MoveAtVelocity(serial_number)

    return output


SBC_MoveJog = lib.SBC_MoveJog
SBC_MoveJog.restype = c_short
SBC_MoveJog.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    jogDirection = MOT_TravelDirection()

    output = SBC_MoveJog(serial_number)

    return output


SBC_MoveRelative = lib.SBC_MoveRelative
SBC_MoveRelative.restype = c_short
SBC_MoveRelative.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    displacement = c_int()

    output = SBC_MoveRelative(serial_number)

    return output


SBC_MoveRelativeDistance = lib.SBC_MoveRelativeDistance
SBC_MoveRelativeDistance.restype = c_short
SBC_MoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_MoveRelativeDistance(serial_number)

    return output


SBC_MoveToPosition = lib.SBC_MoveToPosition
SBC_MoveToPosition.restype = c_short
SBC_MoveToPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    index = c_int()

    output = SBC_MoveToPosition(serial_number)

    return output


SBC_NeedsHoming = lib.SBC_NeedsHoming
SBC_NeedsHoming.restype = c_bool
SBC_NeedsHoming.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_NeedsHoming(serial_number)

    return output


SBC_Open = lib.SBC_Open
SBC_Open.restype = c_short
SBC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    '''
    Open the device for communications.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_Open(serial_number)

    return output


SBC_PersistSettings = lib.SBC_PersistSettings
SBC_PersistSettings.restype = c_bool
SBC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    '''
    Persist device settings to device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_PersistSettings(serial_number)

    return output


SBC_PollingDuration = lib.SBC_PollingDuration
SBC_PollingDuration.restype = c_long
SBC_PollingDuration.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_PollingDuration(serial_number)

    return output


SBC_RegisterMessageCallback = lib.SBC_RegisterMessageCallback
SBC_RegisterMessageCallback.restype = c_short
SBC_RegisterMessageCallback.argtypes = [POINTER(c_char)]


def register_message_callback(serial_number):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        None

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RegisterMessageCallback(serial_number)

    return output


SBC_RequestBacklash = lib.SBC_RequestBacklash
SBC_RequestBacklash.restype = c_short
SBC_RequestBacklash.argtypes = [POINTER(c_char)]


def request_backlash(serial_number):
    '''
    Requests the backlash.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestBacklash(serial_number)

    return output


SBC_RequestBowIndex = lib.SBC_RequestBowIndex
SBC_RequestBowIndex.restype = c_short
SBC_RequestBowIndex.argtypes = [POINTER(c_char)]


def request_bow_index(serial_number):
    '''
    Requests the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestBowIndex(serial_number)

    return output


SBC_RequestDigitalOutputs = lib.SBC_RequestDigitalOutputs
SBC_RequestDigitalOutputs.restype = c_short
SBC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestDigitalOutputs(serial_number)

    return output


SBC_RequestEncoderCounter = lib.SBC_RequestEncoderCounter
SBC_RequestEncoderCounter.restype = c_short
SBC_RequestEncoderCounter.argtypes = [POINTER(c_char)]


def request_encoder_counter(serial_number):
    '''
    Requests the encoder counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestEncoderCounter(serial_number)

    return output


SBC_RequestHomingParams = lib.SBC_RequestHomingParams
SBC_RequestHomingParams.restype = c_short
SBC_RequestHomingParams.argtypes = [POINTER(c_char)]


def request_homing_params(serial_number):
    '''
    Requests the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestHomingParams(serial_number)

    return output


SBC_RequestInputVoltage = lib.SBC_RequestInputVoltage
SBC_RequestInputVoltage.restype = c_short
SBC_RequestInputVoltage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestInputVoltage(serial_number)

    return output


SBC_RequestJogParams = lib.SBC_RequestJogParams
SBC_RequestJogParams.restype = c_short
SBC_RequestJogParams.argtypes = [POINTER(c_char)]


def request_jog_params(serial_number):
    '''
    Requests the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestJogParams(serial_number)

    return output


SBC_RequestJoystickParams = lib.SBC_RequestJoystickParams
SBC_RequestJoystickParams.restype = c_short
SBC_RequestJoystickParams.argtypes = [POINTER(c_char)]


def request_joystick_params(serial_number):
    '''
    Requests the joystick parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestJoystickParams(serial_number)

    return output


SBC_RequestLimitSwitchParams = lib.SBC_RequestLimitSwitchParams
SBC_RequestLimitSwitchParams.restype = c_short
SBC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]


def request_limit_switch_params(serial_number):
    '''
    Requests the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestLimitSwitchParams(serial_number)

    return output


SBC_RequestMoveAbsolutePosition = lib.SBC_RequestMoveAbsolutePosition
SBC_RequestMoveAbsolutePosition.restype = c_short
SBC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


def request_move_absolute_position(serial_number):
    '''
    Requests the position of next absolute move.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestMoveAbsolutePosition(serial_number)

    return output


SBC_RequestMoveRelativeDistance = lib.SBC_RequestMoveRelativeDistance
SBC_RequestMoveRelativeDistance.restype = c_short
SBC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


def request_move_relative_distance(serial_number):
    '''
    Requests the relative move distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestMoveRelativeDistance(serial_number)

    return output


SBC_RequestPIDLoopEncoderParams = lib.SBC_RequestPIDLoopEncoderParams
SBC_RequestPIDLoopEncoderParams.restype = c_short
SBC_RequestPIDLoopEncoderParams.argtypes = [POINTER(c_char)]


def request_p_i_d_loop_encoder_params(serial_number):
    '''
    Requests the Encoder PID loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestPIDLoopEncoderParams(serial_number)

    return output


SBC_RequestPosition = lib.SBC_RequestPosition
SBC_RequestPosition.restype = c_short
SBC_RequestPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestPosition(serial_number)

    return output


SBC_RequestPowerParams = lib.SBC_RequestPowerParams
SBC_RequestPowerParams.restype = c_short
SBC_RequestPowerParams.argtypes = [POINTER(c_char)]


def request_power_params(serial_number):
    '''
    Requests the power parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestPowerParams(serial_number)

    return output


SBC_RequestRackDigitalOutputs = lib.SBC_RequestRackDigitalOutputs
SBC_RequestRackDigitalOutputs.restype = c_short
SBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


def request_rack_digital_outputs(serial_number):
    '''
    Requests the rack digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_RequestRackDigitalOutputs(serial_number)

    return output


SBC_RequestRackStatusBits = lib.SBC_RequestRackStatusBits
SBC_RequestRackStatusBits.restype = c_short
SBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]


def request_rack_status_bits(serial_number):
    '''
    Requests the Rack status bits be downloaded.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = SBC_RequestRackStatusBits(serial_number)

    return output


SBC_RequestSettings = lib.SBC_RequestSettings
SBC_RequestSettings.restype = c_short
SBC_RequestSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestSettings(serial_number)

    return output


SBC_RequestStatusBits = lib.SBC_RequestStatusBits
SBC_RequestStatusBits.restype = c_short
SBC_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestStatusBits(serial_number)

    return output


SBC_RequestTriggerSwitches = lib.SBC_RequestTriggerSwitches
SBC_RequestTriggerSwitches.restype = c_short
SBC_RequestTriggerSwitches.argtypes = [POINTER(c_char)]


def request_trigger_switches(serial_number):
    '''
    Requests the trigger switch parameter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestTriggerSwitches(serial_number)

    return output


SBC_RequestVelParams = lib.SBC_RequestVelParams
SBC_RequestVelParams.restype = c_short
SBC_RequestVelParams.argtypes = [POINTER(c_char)]


def request_vel_params(serial_number):
    '''
    Requests the velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_RequestVelParams(serial_number)

    return output


SBC_ResetRotationModes = lib.SBC_ResetRotationModes
SBC_ResetRotationModes.restype = c_short
SBC_ResetRotationModes.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_ResetRotationModes(serial_number)

    return output


SBC_ResumeMoveMessages = lib.SBC_ResumeMoveMessages
SBC_ResumeMoveMessages.restype = c_short
SBC_ResumeMoveMessages.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_ResumeMoveMessages(serial_number)

    return output


SBC_SetBacklash = lib.SBC_SetBacklash
SBC_SetBacklash.restype = c_short
SBC_SetBacklash.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    distance = c_long()

    output = SBC_SetBacklash(serial_number)

    return output


SBC_SetBowIndex = lib.SBC_SetBowIndex
SBC_SetBowIndex.restype = c_short
SBC_SetBowIndex.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    bowIndex = c_short()

    output = SBC_SetBowIndex(serial_number)

    return output


SBC_SetCalibrationFile = lib.SBC_SetCalibrationFile
SBC_SetCalibrationFile.restype = c_void_p
SBC_SetCalibrationFile.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    filename = POINTER(c_char)()
    enabled = c_bool()

    output = SBC_SetCalibrationFile(serial_number)

    return output


SBC_SetDigitalOutputs = lib.SBC_SetDigitalOutputs
SBC_SetDigitalOutputs.restype = c_short
SBC_SetDigitalOutputs.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    outputsBits = c_byte()

    output = SBC_SetDigitalOutputs(serial_number)

    return output


SBC_SetDirection = lib.SBC_SetDirection
SBC_SetDirection.restype = c_short
SBC_SetDirection.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    reverse = c_bool()

    output = SBC_SetDirection(serial_number)

    return output


SBC_SetEncoderCounter = lib.SBC_SetEncoderCounter
SBC_SetEncoderCounter.restype = c_short
SBC_SetEncoderCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    count = c_long()

    output = SBC_SetEncoderCounter(serial_number)

    return output


SBC_SetHomingParamsBlock = lib.SBC_SetHomingParamsBlock
SBC_SetHomingParamsBlock.restype = c_short
SBC_SetHomingParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = SBC_SetHomingParamsBlock(serial_number)

    return output


SBC_SetHomingVelocity = lib.SBC_SetHomingVelocity
SBC_SetHomingVelocity.restype = c_short
SBC_SetHomingVelocity.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    velocity = c_uint()

    output = SBC_SetHomingVelocity(serial_number)

    return output


SBC_SetJogMode = lib.SBC_SetJogMode
SBC_SetJogMode.restype = c_short
SBC_SetJogMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SBC_SetJogMode(serial_number)

    return output


SBC_SetJogParamsBlock = lib.SBC_SetJogParamsBlock
SBC_SetJogParamsBlock.restype = c_short
SBC_SetJogParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    jogParams = MOT_JogParameters()
    jogParameters = MOT_JogParameters()

    output = SBC_SetJogParamsBlock(serial_number)

    return output


SBC_SetJogStepSize = lib.SBC_SetJogStepSize
SBC_SetJogStepSize.restype = c_short
SBC_SetJogStepSize.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    stepSize = c_uint()

    output = SBC_SetJogStepSize(serial_number)

    return output


SBC_SetJogVelParams = lib.SBC_SetJogVelParams
SBC_SetJogVelParams.restype = c_short
SBC_SetJogVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_SetJogVelParams(serial_number)

    return output


SBC_SetJoystickParams = lib.SBC_SetJoystickParams
SBC_SetJoystickParams.restype = c_short
SBC_SetJoystickParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    joystickParams = MOT_JoystickParameters()

    output = SBC_SetJoystickParams(serial_number)

    return output


SBC_SetLimitSwitchParams = lib.SBC_SetLimitSwitchParams
SBC_SetLimitSwitchParams.restype = c_short
SBC_SetLimitSwitchParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
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
SBC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SBC_SetLimitSwitchParamsBlock(serial_number)

    return output


SBC_SetLimitsSoftwareApproachPolicy = lib.SBC_SetLimitsSoftwareApproachPolicy
SBC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SBC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = SBC_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


SBC_SetMotorParams = lib.SBC_SetMotorParams
SBC_SetMotorParams.restype = c_short
SBC_SetMotorParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SBC_SetMotorParams(serial_number)

    return output


SBC_SetMotorParamsExt = lib.SBC_SetMotorParamsExt
SBC_SetMotorParamsExt.restype = c_short
SBC_SetMotorParamsExt.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SBC_SetMotorParamsExt(serial_number)

    return output


SBC_SetMotorTravelLimits = lib.SBC_SetMotorTravelLimits
SBC_SetMotorTravelLimits.restype = c_short
SBC_SetMotorTravelLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = SBC_SetMotorTravelLimits(serial_number)

    return output


SBC_SetMotorTravelMode = lib.SBC_SetMotorTravelMode
SBC_SetMotorTravelMode.restype = c_short
SBC_SetMotorTravelMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    travelMode = MOT_TravelModes()

    output = SBC_SetMotorTravelMode(serial_number)

    return output


SBC_SetMotorVelocityLimits = lib.SBC_SetMotorVelocityLimits
SBC_SetMotorVelocityLimits.restype = c_short
SBC_SetMotorVelocityLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SBC_SetMotorVelocityLimits(serial_number)

    return output


SBC_SetMoveAbsolutePosition = lib.SBC_SetMoveAbsolutePosition
SBC_SetMoveAbsolutePosition.restype = c_short
SBC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    position = c_int()

    output = SBC_SetMoveAbsolutePosition(serial_number)

    return output


SBC_SetMoveRelativeDistance = lib.SBC_SetMoveRelativeDistance
SBC_SetMoveRelativeDistance.restype = c_short
SBC_SetMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    distance = c_int()

    output = SBC_SetMoveRelativeDistance(serial_number)

    return output


SBC_SetPIDLoopEncoderCoeff = lib.SBC_SetPIDLoopEncoderCoeff
SBC_SetPIDLoopEncoderCoeff.restype = c_short
SBC_SetPIDLoopEncoderCoeff.argtypes = [POINTER(c_char)]


def set_p_i_d_loop_encoder_coeff(serial_number):
    '''
    Sets the Encoder PID loop encoder coefficient.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        coeff: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    coeff = c_double()

    output = SBC_SetPIDLoopEncoderCoeff(serial_number)

    return output


SBC_SetPIDLoopEncoderParams = lib.SBC_SetPIDLoopEncoderParams
SBC_SetPIDLoopEncoderParams.restype = c_short
SBC_SetPIDLoopEncoderParams.argtypes = [POINTER(c_char)]


def set_p_i_d_loop_encoder_params(serial_number):
    '''
    Sets the Encoder PID loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        params: MOT_PIDLoopEncoderParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    params = MOT_PIDLoopEncoderParams()

    output = SBC_SetPIDLoopEncoderParams(serial_number)

    return output


SBC_SetPositionCounter = lib.SBC_SetPositionCounter
SBC_SetPositionCounter.restype = c_short
SBC_SetPositionCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    count = c_long()

    output = SBC_SetPositionCounter(serial_number)

    return output


SBC_SetPowerParams = lib.SBC_SetPowerParams
SBC_SetPowerParams.restype = c_short
SBC_SetPowerParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    powerParams = MOT_PowerParameters()

    output = SBC_SetPowerParams(serial_number)

    return output


SBC_SetRackDigitalOutputs = lib.SBC_SetRackDigitalOutputs
SBC_SetRackDigitalOutputs.restype = c_short
SBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def set_rack_digital_outputs(serial_number):
    '''
    Sets the rack digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        outputsBits: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    outputsBits = c_byte()

    output = SBC_SetRackDigitalOutputs(serial_number)

    return output


SBC_SetRotationModes = lib.SBC_SetRotationModes
SBC_SetRotationModes.restype = c_short
SBC_SetRotationModes.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = SBC_SetRotationModes(serial_number)

    return output


SBC_SetStageAxisLimits = lib.SBC_SetStageAxisLimits
SBC_SetStageAxisLimits.restype = c_short
SBC_SetStageAxisLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    minPosition = c_int()
    maxPosition = c_int()

    output = SBC_SetStageAxisLimits(serial_number)

    return output


SBC_SetTriggerSwitches = lib.SBC_SetTriggerSwitches
SBC_SetTriggerSwitches.restype = c_short
SBC_SetTriggerSwitches.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    indicatorBits = c_byte()

    output = SBC_SetTriggerSwitches(serial_number)

    return output


SBC_SetVelParams = lib.SBC_SetVelParams
SBC_SetVelParams.restype = c_short
SBC_SetVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = SBC_SetVelParams(serial_number)

    return output


SBC_SetVelParamsBlock = lib.SBC_SetVelParamsBlock
SBC_SetVelParamsBlock.restype = c_short
SBC_SetVelParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    velocityParams = MOT_VelocityParameters()
    velocityParameters = MOT_VelocityParameters()

    output = SBC_SetVelParamsBlock(serial_number)

    return output


SBC_StartPolling = lib.SBC_StartPolling
SBC_StartPolling.restype = c_bool
SBC_StartPolling.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    milliseconds = c_int()

    output = SBC_StartPolling(serial_number)

    return output


SBC_StopImmediate = lib.SBC_StopImmediate
SBC_StopImmediate.restype = c_short
SBC_StopImmediate.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_StopImmediate(serial_number)

    return output


SBC_StopPolling = lib.SBC_StopPolling
SBC_StopPolling.restype = c_void_p
SBC_StopPolling.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_StopPolling(serial_number)

    return output


SBC_StopProfiled = lib.SBC_StopProfiled
SBC_StopProfiled.restype = c_short
SBC_StopProfiled.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_StopProfiled(serial_number)

    return output


SBC_SuspendMoveMessages = lib.SBC_SuspendMoveMessages
SBC_SuspendMoveMessages.restype = c_short
SBC_SuspendMoveMessages.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_SuspendMoveMessages(serial_number)

    return output


SBC_TimeSinceLastMsgReceived = lib.SBC_TimeSinceLastMsgReceived
SBC_TimeSinceLastMsgReceived.restype = c_bool
SBC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


def time_since_last_msg_received(serial_number):
    '''
    Gets the time in milliseconds since tha last message was received from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        lastUpdateTimeMS: c_int64

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    lastUpdateTimeMS = c_int64()

    output = SBC_TimeSinceLastMsgReceived(serial_number)

    return output


SBC_UsesPIDLoopEncoding = lib.SBC_UsesPIDLoopEncoding
SBC_UsesPIDLoopEncoding.restype = c_bool
SBC_UsesPIDLoopEncoding.argtypes = [POINTER(c_char)]


def uses_p_i_d_loop_encoding(serial_number):
    '''
    Determines if we can uses PID loop encoding.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = SBC_UsesPIDLoopEncoding(serial_number)

    return output


SBC_WaitForMessage = lib.SBC_WaitForMessage
SBC_WaitForMessage.restype = c_bool
SBC_WaitForMessage.argtypes = [POINTER(c_char)]


def wait_for_message(serial_number):
    '''
    Get the next MessageQueue item if it is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SBC_WaitForMessage(serial_number)

    return output


TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = []


def build_device_list():
    '''
    Build the DeviceList.

    Parameters
    ----------
        None

    Returns
    -------
        c_short
    '''


    output = TLI_BuildDeviceList()

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char)]


def get_device_info(serial_number):
    '''
    Get the device information from the USB port.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        serialNumber: POINTER(c_char)
        info: TLI_DeviceInfo

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    serialNumber = POINTER(c_char)()
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number)

    return output


TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]


def get_device_list(stringsReceiver):
    '''
    Get the entire contents of the device list.

    Parameters
    ----------
        stringsReceiver: SafeArray

    Returns
    -------
        c_short
    '''

    stringsReceiver = SafeArray()

    output = TLI_GetDeviceList(stringsReceiver)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray]


def get_device_list_by_type(stringsReceiver):
    '''
    Get the contents of the device list which match the supplied typeID.

    Parameters
    ----------
        stringsReceiver: SafeArray
        typeID: c_int

    Returns
    -------
        c_short
    '''

    stringsReceiver = SafeArray()
    typeID = c_int()

    output = TLI_GetDeviceListByType(stringsReceiver)

    return output


TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char)]


def get_device_list_by_type_ext(receiveBuffer):
    '''
    Get the contents of the device list which match the supplied typeID.

    Parameters
    ----------
        receiveBuffer: POINTER(c_char)
        sizeOfBuffer: c_ulong
        typeID: c_int

    Returns
    -------
        c_short
    '''

    receiveBuffer = POINTER(c_char)()
    sizeOfBuffer = c_ulong()
    typeID = c_int()

    output = TLI_GetDeviceListByTypeExt(receiveBuffer)

    return output


TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray]


def get_device_list_by_types(stringsReceiver):
    '''
    Get the contents of the device list which match the supplied typeIDs.

    Parameters
    ----------
        stringsReceiver: SafeArray
        typeIDs: c_int
        length: c_int

    Returns
    -------
        c_short
    '''

    stringsReceiver = SafeArray()
    typeIDs = c_int()
    length = c_int()

    output = TLI_GetDeviceListByTypes(stringsReceiver)

    return output


TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char)]


def get_device_list_by_types_ext(receiveBuffer):
    '''
    Get the contents of the device list which match the supplied typeIDs.

    Parameters
    ----------
        receiveBuffer: POINTER(c_char)
        sizeOfBuffer: c_ulong
        typeIDs: c_int
        length: c_int

    Returns
    -------
        c_short
    '''

    receiveBuffer = POINTER(c_char)()
    sizeOfBuffer = c_ulong()
    typeIDs = c_int()
    length = c_int()

    output = TLI_GetDeviceListByTypesExt(receiveBuffer)

    return output


TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char)]


def get_device_list_ext(receiveBuffer):
    '''
    Get the entire contents of the device list.

    Parameters
    ----------
        receiveBuffer: POINTER(c_char)
        sizeOfBuffer: c_ulong

    Returns
    -------
        c_short
    '''

    receiveBuffer = POINTER(c_char)()
    sizeOfBuffer = c_ulong()

    output = TLI_GetDeviceListExt(receiveBuffer)

    return output


TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short
TLI_GetDeviceListSize.argtypes = []


def get_device_list_size():
    '''
    Gets the device list size.

    Parameters
    ----------

    Returns
    -------
        c_short
    '''


    output = TLI_GetDeviceListSize()

    return output


TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p
TLI_InitializeSimulations.argtypes = []


def initialize_simulations():
    '''
    Initialize a connection to the Simulation Manager, which must already be running.

    Parameters
    ----------

    Returns
    -------
        c_void_p
    '''


    output = TLI_InitializeSimulations()

    return output


