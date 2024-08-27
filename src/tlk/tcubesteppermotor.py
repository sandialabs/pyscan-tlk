from ctypes import (
    POINTER,
    c_bool,
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
    KST_Stages,
    MOT_ButtonModes,
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

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.StepperMotor.DLL")

SCC_CanHome = lib.SCC_CanHome
SCC_CanHome.restype = c_bool
SCC_CanHome.argtypes = []


def can_home(serial_number):
    '''
    Can the device perform a Home.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_CanHome(serial_number)

    return output


SCC_CanMoveWithoutHomingFirst = lib.SCC_CanMoveWithoutHomingFirst
SCC_CanMoveWithoutHomingFirst.restype = c_bool
SCC_CanMoveWithoutHomingFirst.argtypes = []


def can_move_without_homing_first(serial_number):
    '''
    Can this device be moved without Homing.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_CanMoveWithoutHomingFirst(serial_number)

    return output


SCC_CheckConnection = lib.SCC_CheckConnection
SCC_CheckConnection.restype = c_bool
SCC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    '''
    Check connection.

    Parameters
    ----------
    serial_number - int
        serial_number of instrument

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_CheckConnection(serial_number)

    return output


SCC_ClearMessageQueue = lib.SCC_ClearMessageQueue
SCC_ClearMessageQueue.restype = c_void_p
SCC_ClearMessageQueue.argtypes = []


def clear_message_queue(serial_number):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_ClearMessageQueue(serial_number)

    return output


SCC_Close = lib.SCC_Close
SCC_Close.restype = c_void_p
SCC_Close.argtypes = []


def close_device(serial_number):
    '''
    Disconnect and close the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_Close(serial_number)

    return output


SCC_DisableChannel = lib.SCC_DisableChannel
SCC_DisableChannel.restype = c_short
SCC_DisableChannel.argtypes = []


def disable_channel(serial_number):
    '''
    Disable the channel so that motor can be moved by hand.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_DisableChannel(serial_number)

    return output


SCC_EnableChannel = lib.SCC_EnableChannel
SCC_EnableChannel.restype = c_short
SCC_EnableChannel.argtypes = []


def enable_channel(serial_number):
    '''
    Enable channel for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_EnableChannel(serial_number)

    return output


SCC_EnableLastMsgTimer = lib.SCC_EnableLastMsgTimer
SCC_EnableLastMsgTimer.restype = c_void_p
SCC_EnableLastMsgTimer.argtypes = []


def enable_last_msg_timer(serial_number):
    '''
    Enables the last message monitoring timer.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        enable: c_bool
        lastMsgTimeout: c_int32

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SCC_EnableLastMsgTimer(serial_number)

    return output


SCC_GetBacklash = lib.SCC_GetBacklash
SCC_GetBacklash.restype = c_long
SCC_GetBacklash.argtypes = []


def get_backlash(serial_number):
    '''
    Get the backlash distance setting (used to control hysteresis).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetBacklash(serial_number)

    return output


SCC_GetBowIndex = lib.SCC_GetBowIndex
SCC_GetBowIndex.restype = c_short
SCC_GetBowIndex.argtypes = []


def get_bow_index(serial_number):
    '''
    Gets the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetBowIndex(serial_number)

    return output


SCC_GetButtonParams = lib.SCC_GetButtonParams
SCC_GetButtonParams.restype = c_short
SCC_GetButtonParams.argtypes = []


def get_button_params(serial_number):
    '''
    Gets the TCube button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonMode: MOT_ButtonModes
        leftButtonPosition: c_int
        rightButtonPosition: c_int
        timeout: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()
    timeout = c_short()

    output = SCC_GetButtonParams(serial_number)

    return output


SCC_GetButtonParamsBlock = lib.SCC_GetButtonParamsBlock
SCC_GetButtonParamsBlock.restype = c_short
SCC_GetButtonParamsBlock.argtypes = []


def get_button_params_block(serial_number):
    '''
    Get the button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonParams: MOT_ButtonParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonParams = MOT_ButtonParameters()

    output = SCC_GetButtonParamsBlock(serial_number)

    return output


SCC_GetCalibrationFile = lib.SCC_GetCalibrationFile
SCC_GetCalibrationFile.restype = c_bool
SCC_GetCalibrationFile.argtypes = []


def get_calibration_file(serial_number):
    '''
    Get calibration file for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        filename: POINTER(c_char)
        sizeOfBuffer: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    filename = POINTER(c_char)()
    sizeOfBuffer = c_short()

    output = SCC_GetCalibrationFile(serial_number)

    return output


SCC_GetDeviceUnitFromRealValue = lib.SCC_GetDeviceUnitFromRealValue
SCC_GetDeviceUnitFromRealValue.restype = c_short
SCC_GetDeviceUnitFromRealValue.argtypes = []


def get_device_unit_from_real_value(serial_number):
    '''
    Converts a device unit to a real world unit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        real_unit: c_double
        device_unit: c_int
        unitType: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = SCC_GetDeviceUnitFromRealValue(serial_number)

    return output


SCC_GetEncoderCounter = lib.SCC_GetEncoderCounter
SCC_GetEncoderCounter.restype = c_long
SCC_GetEncoderCounter.argtypes = []


def get_encoder_counter(serial_number):
    '''
    Get the Encoder Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetEncoderCounter(serial_number)

    return output


SCC_GetHardwareInfo = lib.SCC_GetHardwareInfo
SCC_GetHardwareInfo.restype = c_short
SCC_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
    serial_number - int
        serial_number of instrument

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = SCC_GetHardwareInfo(serial_number)

    return output


SCC_GetHardwareInfoBlock = lib.SCC_GetHardwareInfoBlock
SCC_GetHardwareInfoBlock.restype = c_short
SCC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
    serial_number - int
        serial_number of instrument

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    hardwareInfo = TLI_HardwareInformation()

    output = SCC_GetHardwareInfoBlock(serial_number)

    return output


SCC_GetHomingParamsBlock = lib.SCC_GetHomingParamsBlock
SCC_GetHomingParamsBlock.restype = c_short
SCC_GetHomingParamsBlock.argtypes = []


def get_homing_params_block(serial_number):
    '''
    Get the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        homingParams: MOT_HomingParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    homingParams = MOT_HomingParameters()

    output = SCC_GetHomingParamsBlock(serial_number)

    return output


SCC_GetHomingVelocity = lib.SCC_GetHomingVelocity
SCC_GetHomingVelocity.restype = c_uint
SCC_GetHomingVelocity.argtypes = []


def get_homing_velocity(serial_number):
    '''
    Gets the homing velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetHomingVelocity(serial_number)

    return output


SCC_GetHubBay = lib.SCC_GetHubBay
SCC_GetHubBay.restype = POINTER(c_char)
SCC_GetHubBay.argtypes = []


def get_hub_bay(serial_number):
    '''
    Gets the hub bay number this device is fitted to.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        POINTER(c_char)
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetHubBay(serial_number)

    return output


SCC_GetJogMode = lib.SCC_GetJogMode
SCC_GetJogMode.restype = c_short
SCC_GetJogMode.argtypes = []


def get_jog_mode(serial_number):
    '''
    Gets the jog mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: MOT_JogModes
        stopMode: MOT_StopModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SCC_GetJogMode(serial_number)

    return output


SCC_GetJogParamsBlock = lib.SCC_GetJogParamsBlock
SCC_GetJogParamsBlock.restype = c_short
SCC_GetJogParamsBlock.argtypes = []


def get_jog_params_block(serial_number):
    '''
    Get the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        jogParams: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    jogParams = MOT_JogParameters()

    output = SCC_GetJogParamsBlock(serial_number)

    return output


SCC_GetJogStepSize = lib.SCC_GetJogStepSize
SCC_GetJogStepSize.restype = c_uint
SCC_GetJogStepSize.argtypes = []


def get_jog_step_size(serial_number):
    '''
    Gets the distance to move when jogging.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetJogStepSize(serial_number)

    return output


SCC_GetJogVelParams = lib.SCC_GetJogVelParams
SCC_GetJogVelParams.restype = c_short
SCC_GetJogVelParams.argtypes = []


def get_jog_vel_params(serial_number):
    '''
    Gets the jog velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_GetJogVelParams(serial_number)

    return output


SCC_GetLEDswitches = lib.SCC_GetLEDswitches
SCC_GetLEDswitches.restype = c_long
SCC_GetLEDswitches.argtypes = []


def get_l_e_dswitches(serial_number):
    '''
    Get the LED indicator bits on cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetLEDswitches(serial_number)

    return output


SCC_GetLimitSwitchParams = lib.SCC_GetLimitSwitchParams
SCC_GetLimitSwitchParams.restype = c_short
SCC_GetLimitSwitchParams.argtypes = []


def get_limit_switch_params(serial_number):
    '''
    Gets the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
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
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = SCC_GetLimitSwitchParams(serial_number)

    return output


SCC_GetLimitSwitchParamsBlock = lib.SCC_GetLimitSwitchParamsBlock
SCC_GetLimitSwitchParamsBlock.restype = c_short
SCC_GetLimitSwitchParamsBlock.argtypes = []


def get_limit_switch_params_block(serial_number):
    '''
    Get the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        limitSwitchParams: MOT_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SCC_GetLimitSwitchParamsBlock(serial_number)

    return output


SCC_GetMotorParams = lib.SCC_GetMotorParams
SCC_GetMotorParams.restype = c_short
SCC_GetMotorParams.argtypes = []


def get_motor_params(serial_number):
    '''
    Gets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_long
        gearBoxRatio: c_long
        pitch: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SCC_GetMotorParams(serial_number)

    return output


SCC_GetMotorParamsExt = lib.SCC_GetMotorParamsExt
SCC_GetMotorParamsExt.restype = c_short
SCC_GetMotorParamsExt.argtypes = []


def get_motor_params_ext(serial_number):
    '''
    Gets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_double
        gearBoxRatio: c_double
        pitch: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SCC_GetMotorParamsExt(serial_number)

    return output


SCC_GetMotorTravelLimits = lib.SCC_GetMotorTravelLimits
SCC_GetMotorTravelLimits.restype = c_short
SCC_GetMotorTravelLimits.argtypes = []


def get_motor_travel_limits(serial_number):
    '''
    Gets the absolute minimum and maximum travel range constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        minPosition: c_double
        maxPosition: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    minPosition = c_double()
    maxPosition = c_double()

    output = SCC_GetMotorTravelLimits(serial_number)

    return output


SCC_GetMotorTravelMode = lib.SCC_GetMotorTravelMode
SCC_GetMotorTravelMode.restype = MOT_TravelModes
SCC_GetMotorTravelMode.argtypes = []


def get_motor_travel_mode(serial_number):
    '''
    Get the motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        MOT_TravelModes
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetMotorTravelMode(serial_number)

    return output


SCC_GetMotorVelocityLimits = lib.SCC_GetMotorVelocityLimits
SCC_GetMotorVelocityLimits.restype = c_short
SCC_GetMotorVelocityLimits.argtypes = []


def get_motor_velocity_limits(serial_number):
    '''
    Gets the absolute maximum velocity and acceleration constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxVelocity: c_double
        maxAcceleration: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SCC_GetMotorVelocityLimits(serial_number)

    return output


SCC_GetMoveAbsolutePosition = lib.SCC_GetMoveAbsolutePosition
SCC_GetMoveAbsolutePosition.restype = c_int
SCC_GetMoveAbsolutePosition.argtypes = []


def get_move_absolute_position(serial_number):
    '''
    Gets the move absolute position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetMoveAbsolutePosition(serial_number)

    return output


SCC_GetMoveRelativeDistance = lib.SCC_GetMoveRelativeDistance
SCC_GetMoveRelativeDistance.restype = c_int
SCC_GetMoveRelativeDistance.argtypes = []


def get_move_relative_distance(serial_number):
    '''
    Gets the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetMoveRelativeDistance(serial_number)

    return output


SCC_GetNextMessage = lib.SCC_GetNextMessage
SCC_GetNextMessage.restype = c_bool
SCC_GetNextMessage.argtypes = []


def get_next_message(serial_number):
    '''
    Get the next MessageQueue item.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SCC_GetNextMessage(serial_number)

    return output


SCC_GetNumberPositions = lib.SCC_GetNumberPositions
SCC_GetNumberPositions.restype = c_int
SCC_GetNumberPositions.argtypes = []


def get_number_positions(serial_number):
    '''
    Get number of positions.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetNumberPositions(serial_number)

    return output


SCC_GetPosition = lib.SCC_GetPosition
SCC_GetPosition.restype = c_int
SCC_GetPosition.argtypes = []


def get_position(serial_number):
    '''
    Get the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetPosition(serial_number)

    return output


SCC_GetPositionCounter = lib.SCC_GetPositionCounter
SCC_GetPositionCounter.restype = c_long
SCC_GetPositionCounter.argtypes = []


def get_position_counter(serial_number):
    '''
    Get the Position Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetPositionCounter(serial_number)

    return output


SCC_GetPotentiometerParams = lib.SCC_GetPotentiometerParams
SCC_GetPotentiometerParams.restype = c_short
SCC_GetPotentiometerParams.argtypes = []


def get_potentiometer_params(serial_number):
    '''
    Gets the potentiometer parameters for the TCube.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_short
        thresholdDeflection: c_long
        velocity: c_ulong

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = SCC_GetPotentiometerParams(serial_number)

    return output


SCC_GetPotentiometerParamsBlock = lib.SCC_GetPotentiometerParamsBlock
SCC_GetPotentiometerParamsBlock.restype = c_short
SCC_GetPotentiometerParamsBlock.argtypes = []


def get_potentiometer_params_block(serial_number):
    '''
    Get the potentiometer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        potentiometerSteps: MOT_PotentiometerSteps

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = SCC_GetPotentiometerParamsBlock(serial_number)

    return output


SCC_GetPowerParams = lib.SCC_GetPowerParams
SCC_GetPowerParams.restype = c_short
SCC_GetPowerParams.argtypes = []


def get_power_params(serial_number):
    '''
    Gets the power parameters for the stepper motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        powerParams: MOT_PowerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    powerParams = MOT_PowerParameters()

    output = SCC_GetPowerParams(serial_number)

    return output


SCC_GetRealValueFromDeviceUnit = lib.SCC_GetRealValueFromDeviceUnit
SCC_GetRealValueFromDeviceUnit.restype = c_short
SCC_GetRealValueFromDeviceUnit.argtypes = []


def get_real_value_from_device_unit(serial_number):
    '''
    Converts a device unit to a real world unit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        device_unit: c_int
        real_unit: c_double
        unitType: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = SCC_GetRealValueFromDeviceUnit(serial_number)

    return output


SCC_GetSoftLimitMode = lib.SCC_GetSoftLimitMode
SCC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
SCC_GetSoftLimitMode.argtypes = []


def get_soft_limit_mode(serial_number):
    '''
    Gets the software limits mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        MOT_LimitsSoftwareApproachPolicy
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetSoftLimitMode(serial_number)

    return output


SCC_GetSoftwareVersion = lib.SCC_GetSoftwareVersion
SCC_GetSoftwareVersion.restype = c_ulong
SCC_GetSoftwareVersion.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetSoftwareVersion(serial_number)

    return output


SCC_GetStageAxisMaxPos = lib.SCC_GetStageAxisMaxPos
SCC_GetStageAxisMaxPos.restype = c_int
SCC_GetStageAxisMaxPos.argtypes = []


def get_stage_axis_max_pos(serial_number):
    '''
    Gets the Stepper Motor maximum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetStageAxisMaxPos(serial_number)

    return output


SCC_GetStageAxisMinPos = lib.SCC_GetStageAxisMinPos
SCC_GetStageAxisMinPos.restype = c_int
SCC_GetStageAxisMinPos.argtypes = []


def get_stage_axis_min_pos(serial_number):
    '''
    Gets the Stepper Motor minimum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetStageAxisMinPos(serial_number)

    return output


SCC_GetStatusBits = lib.SCC_GetStatusBits
SCC_GetStatusBits.restype = c_ulong
SCC_GetStatusBits.argtypes = []


def get_status_bits(serial_number):
    '''
    Get the current status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_GetStatusBits(serial_number)

    return output


SCC_GetVelParams = lib.SCC_GetVelParams
SCC_GetVelParams.restype = c_short
SCC_GetVelParams.argtypes = []


def get_vel_params(serial_number):
    '''
    Gets the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_GetVelParams(serial_number)

    return output


SCC_GetVelParamsBlock = lib.SCC_GetVelParamsBlock
SCC_GetVelParamsBlock.restype = c_short
SCC_GetVelParamsBlock.argtypes = []


def get_vel_params_block(serial_number):
    '''
    Get the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocityParams: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocityParams = MOT_VelocityParameters()

    output = SCC_GetVelParamsBlock(serial_number)

    return output


SCC_HasLastMsgTimerOverrun = lib.SCC_HasLastMsgTimerOverrun
SCC_HasLastMsgTimerOverrun.restype = c_bool
SCC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by SCC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_HasLastMsgTimerOverrun(serial_number)

    return output


SCC_Home = lib.SCC_Home
SCC_Home.restype = c_short
SCC_Home.argtypes = []


def home(serial_number):
    '''
    Home the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_Home(serial_number)

    return output


SCC_Identify = lib.SCC_Identify
SCC_Identify.restype = c_void_p
SCC_Identify.argtypes = []


def identify(serial_number):
    '''
    Sends a command to the device to make it identify iteself.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_Identify(serial_number)

    return output


SCC_IsCalibrationActive = lib.SCC_IsCalibrationActive
SCC_IsCalibrationActive.restype = c_bool
SCC_IsCalibrationActive.argtypes = []


def is_calibration_active(serial_number):
    '''
    Is a calibration file active for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_IsCalibrationActive(serial_number)

    return output


SCC_LoadNamedSettings = lib.SCC_LoadNamedSettings
SCC_LoadNamedSettings.restype = c_bool
SCC_LoadNamedSettings.argtypes = []


def load_named_settings(serial_number):
    '''
    Update device with named settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        settingsName: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    settingsName = POINTER(c_char)()

    output = SCC_LoadNamedSettings(serial_number)

    return output


SCC_LoadSettings = lib.SCC_LoadSettings
SCC_LoadSettings.restype = c_bool
SCC_LoadSettings.argtypes = []


def load_settings(serial_number):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_LoadSettings(serial_number)

    return output


SCC_MessageQueueSize = lib.SCC_MessageQueueSize
SCC_MessageQueueSize.restype = c_int
SCC_MessageQueueSize.argtypes = []


def message_queue_size(serial_number):
    '''
    Gets the MessageQueue size.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_MessageQueueSize(serial_number)

    return output


SCC_MoveAbsolute = lib.SCC_MoveAbsolute
SCC_MoveAbsolute.restype = c_short
SCC_MoveAbsolute.argtypes = []


def move_absolute(serial_number):
    '''
    Moves the device to the position defined in the SetMoveAbsolute command.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_MoveAbsolute(serial_number)

    return output


SCC_MoveAtVelocity = lib.SCC_MoveAtVelocity
SCC_MoveAtVelocity.restype = c_short
SCC_MoveAtVelocity.argtypes = []


def move_at_velocity(serial_number):
    '''
    Start moving at the current velocity in the specified direction.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        direction: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    direction = MOT_TravelDirection()

    output = SCC_MoveAtVelocity(serial_number)

    return output


SCC_MoveJog = lib.SCC_MoveJog
SCC_MoveJog.restype = c_short
SCC_MoveJog.argtypes = []


def move_jog(serial_number):
    '''
    Perform a jog.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        jogDirection: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    jogDirection = MOT_TravelDirection()

    output = SCC_MoveJog(serial_number)

    return output


SCC_MoveRelative = lib.SCC_MoveRelative
SCC_MoveRelative.restype = c_short
SCC_MoveRelative.argtypes = []


def move_relative(serial_number):
    '''
    Move the motor by a relative amount.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        displacement: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    displacement = c_int()

    output = SCC_MoveRelative(serial_number)

    return output


SCC_MoveRelativeDistance = lib.SCC_MoveRelativeDistance
SCC_MoveRelativeDistance.restype = c_short
SCC_MoveRelativeDistance.argtypes = []


def move_relative_distance(serial_number):
    '''
    Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_MoveRelativeDistance(serial_number)

    return output


SCC_MoveToPosition = lib.SCC_MoveToPosition
SCC_MoveToPosition.restype = c_short
SCC_MoveToPosition.argtypes = []


def move_to_position(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_int()

    output = SCC_MoveToPosition(serial_number)

    return output


SCC_NeedsHoming = lib.SCC_NeedsHoming
SCC_NeedsHoming.restype = c_bool
SCC_NeedsHoming.argtypes = []


def needs_homing(serial_number):
    '''
    Does the device need to be Homed before a move can be performed.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_NeedsHoming(serial_number)

    return output


SCC_Open = lib.SCC_Open
SCC_Open.restype = c_short
SCC_Open.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = SCC_Open(serial_number)

    return output


SCC_PersistSettings = lib.SCC_PersistSettings
SCC_PersistSettings.restype = c_bool
SCC_PersistSettings.argtypes = []


def persist_settings(serial_number):
    '''
    persist the devices current settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_PersistSettings(serial_number)

    return output


SCC_PollingDuration = lib.SCC_PollingDuration
SCC_PollingDuration.restype = c_long
SCC_PollingDuration.argtypes = []


def polling_duration(serial_number):
    '''
    Gets the polling loop duration.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_PollingDuration(serial_number)

    return output


SCC_RegisterMessageCallback = lib.SCC_RegisterMessageCallback
SCC_RegisterMessageCallback.restype = c_void_p
SCC_RegisterMessageCallback.argtypes = []


def register_message_callback(serial_number):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        None

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RegisterMessageCallback(serial_number)

    return output


SCC_RequestBacklash = lib.SCC_RequestBacklash
SCC_RequestBacklash.restype = c_short
SCC_RequestBacklash.argtypes = []


def request_backlash(serial_number):
    '''
    Requests the backlash.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestBacklash(serial_number)

    return output


SCC_RequestBowIndex = lib.SCC_RequestBowIndex
SCC_RequestBowIndex.restype = c_short
SCC_RequestBowIndex.argtypes = []


def request_bow_index(serial_number):
    '''
    Requests the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestBowIndex(serial_number)

    return output


SCC_RequestButtonParams = lib.SCC_RequestButtonParams
SCC_RequestButtonParams.restype = c_short
SCC_RequestButtonParams.argtypes = []


def request_button_params(serial_number):
    '''
    Requests the button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestButtonParams(serial_number)

    return output


SCC_RequestEncoderCounter = lib.SCC_RequestEncoderCounter
SCC_RequestEncoderCounter.restype = c_short
SCC_RequestEncoderCounter.argtypes = []


def request_encoder_counter(serial_number):
    '''
    Requests the encoder counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestEncoderCounter(serial_number)

    return output


SCC_RequestHomingParams = lib.SCC_RequestHomingParams
SCC_RequestHomingParams.restype = c_short
SCC_RequestHomingParams.argtypes = []


def request_homing_params(serial_number):
    '''
    Requests the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestHomingParams(serial_number)

    return output


SCC_RequestJogParams = lib.SCC_RequestJogParams
SCC_RequestJogParams.restype = c_short
SCC_RequestJogParams.argtypes = []


def request_jog_params(serial_number):
    '''
    Requests the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestJogParams(serial_number)

    return output


SCC_RequestLEDswitches = lib.SCC_RequestLEDswitches
SCC_RequestLEDswitches.restype = c_short
SCC_RequestLEDswitches.argtypes = []


def request_l_e_dswitches(serial_number):
    '''
    Request the LED indicator bits on cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestLEDswitches(serial_number)

    return output


SCC_RequestLimitSwitchParams = lib.SCC_RequestLimitSwitchParams
SCC_RequestLimitSwitchParams.restype = c_short
SCC_RequestLimitSwitchParams.argtypes = []


def request_limit_switch_params(serial_number):
    '''
    Requests the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestLimitSwitchParams(serial_number)

    return output


SCC_RequestMoveAbsolutePosition = lib.SCC_RequestMoveAbsolutePosition
SCC_RequestMoveAbsolutePosition.restype = c_short
SCC_RequestMoveAbsolutePosition.argtypes = []


def request_move_absolute_position(serial_number):
    '''
    Requests the position of next absolute move.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestMoveAbsolutePosition(serial_number)

    return output


SCC_RequestMoveRelativeDistance = lib.SCC_RequestMoveRelativeDistance
SCC_RequestMoveRelativeDistance.restype = c_short
SCC_RequestMoveRelativeDistance.argtypes = []


def request_move_relative_distance(serial_number):
    '''
    Requests the relative move distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestMoveRelativeDistance(serial_number)

    return output


SCC_RequestPosition = lib.SCC_RequestPosition
SCC_RequestPosition.restype = c_short
SCC_RequestPosition.argtypes = []


def request_position(serial_number):
    '''
    Requests the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestPosition(serial_number)

    return output


SCC_RequestPotentiometerParams = lib.SCC_RequestPotentiometerParams
SCC_RequestPotentiometerParams.restype = c_short
SCC_RequestPotentiometerParams.argtypes = []


def request_potentiometer_params(serial_number):
    '''
    Requests the potentiometer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestPotentiometerParams(serial_number)

    return output


SCC_RequestPowerParams = lib.SCC_RequestPowerParams
SCC_RequestPowerParams.restype = c_short
SCC_RequestPowerParams.argtypes = []


def request_power_params(serial_number):
    '''
    Requests the power parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestPowerParams(serial_number)

    return output


SCC_RequestSettings = lib.SCC_RequestSettings
SCC_RequestSettings.restype = c_short
SCC_RequestSettings.argtypes = []


def request_settings(serial_number):
    '''
    Requests that all settings are download from device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestSettings(serial_number)

    return output


SCC_RequestStatusBits = lib.SCC_RequestStatusBits
SCC_RequestStatusBits.restype = c_short
SCC_RequestStatusBits.argtypes = []


def request_status_bits(serial_number):
    '''
    Request the status bits which identify the current motor state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestStatusBits(serial_number)

    return output


SCC_RequestVelParams = lib.SCC_RequestVelParams
SCC_RequestVelParams.restype = c_short
SCC_RequestVelParams.argtypes = []


def request_vel_params(serial_number):
    '''
    Requests the velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_RequestVelParams(serial_number)

    return output


SCC_ResetRotationModes = lib.SCC_ResetRotationModes
SCC_ResetRotationModes.restype = c_short
SCC_ResetRotationModes.argtypes = []


def reset_rotation_modes(serial_number):
    '''
    Reset the rotation modes for a rotational device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_ResetRotationModes(serial_number)

    return output


SCC_ResumeMoveMessages = lib.SCC_ResumeMoveMessages
SCC_ResumeMoveMessages.restype = c_short
SCC_ResumeMoveMessages.argtypes = []


def resume_move_messages(serial_number):
    '''
    Resume suspended move messages.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_ResumeMoveMessages(serial_number)

    return output


SCC_SetBacklash = lib.SCC_SetBacklash
SCC_SetBacklash.restype = c_short
SCC_SetBacklash.argtypes = []


def set_backlash(serial_number):
    '''
    Sets the backlash distance (used to control hysteresis).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        distance: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    distance = c_long()

    output = SCC_SetBacklash(serial_number)

    return output


SCC_SetBowIndex = lib.SCC_SetBowIndex
SCC_SetBowIndex.restype = c_short
SCC_SetBowIndex.argtypes = []


def set_bow_index(serial_number):
    '''
    Sets the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        bowIndex: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    bowIndex = c_short()

    output = SCC_SetBowIndex(serial_number)

    return output


SCC_SetButtonParams = lib.SCC_SetButtonParams
SCC_SetButtonParams.restype = c_short
SCC_SetButtonParams.argtypes = []


def set_button_params(serial_number):
    '''
    Sets the TCube button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonMode: MOT_ButtonModes
        leftButtonPosition: c_int
        rightButtonPosition: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()

    output = SCC_SetButtonParams(serial_number)

    return output


SCC_SetButtonParamsBlock = lib.SCC_SetButtonParamsBlock
SCC_SetButtonParamsBlock.restype = c_short
SCC_SetButtonParamsBlock.argtypes = []


def set_button_params_block(serial_number):
    '''
    Set the button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonParams: MOT_ButtonParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonParams = MOT_ButtonParameters()

    output = SCC_SetButtonParamsBlock(serial_number)

    return output


SCC_SetCalibrationFile = lib.SCC_SetCalibrationFile
SCC_SetCalibrationFile.restype = c_void_p
SCC_SetCalibrationFile.argtypes = []


def set_calibration_file(serial_number):
    '''
    Set the calibration file for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        filename: POINTER(c_char)
        enabled: c_bool

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    filename = POINTER(c_char)()
    enabled = c_bool()

    output = SCC_SetCalibrationFile(serial_number)

    return output


SCC_SetDirection = lib.SCC_SetDirection
SCC_SetDirection.restype = c_void_p
SCC_SetDirection.argtypes = []


def set_direction(serial_number):
    '''
    Sets the motor direction sense.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        reverse: c_bool

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    reverse = c_bool()

    output = SCC_SetDirection(serial_number)

    return output


SCC_SetEncoderCounter = lib.SCC_SetEncoderCounter
SCC_SetEncoderCounter.restype = c_short
SCC_SetEncoderCounter.argtypes = []


def set_encoder_counter(serial_number):
    '''
    Set the Encoder Counter values.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        count: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    count = c_long()

    output = SCC_SetEncoderCounter(serial_number)

    return output


SCC_SetHomingParamsBlock = lib.SCC_SetHomingParamsBlock
SCC_SetHomingParamsBlock.restype = c_short
SCC_SetHomingParamsBlock.argtypes = []


def set_homing_params_block(serial_number):
    '''
    Set the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        homingParams: MOT_HomingParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    homingParams = MOT_HomingParameters()

    output = SCC_SetHomingParamsBlock(serial_number)

    return output


SCC_SetHomingVelocity = lib.SCC_SetHomingVelocity
SCC_SetHomingVelocity.restype = c_short
SCC_SetHomingVelocity.argtypes = []


def set_homing_velocity(serial_number):
    '''
    Sets the homing velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocity: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocity = c_uint()

    output = SCC_SetHomingVelocity(serial_number)

    return output


SCC_SetJogMode = lib.SCC_SetJogMode
SCC_SetJogMode.restype = c_short
SCC_SetJogMode.argtypes = []


def set_jog_mode(serial_number):
    '''
    Sets the jog mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: MOT_JogModes
        stopMode: MOT_StopModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = SCC_SetJogMode(serial_number)

    return output


SCC_SetJogParamsBlock = lib.SCC_SetJogParamsBlock
SCC_SetJogParamsBlock.restype = c_short
SCC_SetJogParamsBlock.argtypes = []


def set_jog_params_block(serial_number):
    '''
    Set the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        jogParams: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    jogParams = MOT_JogParameters()

    output = SCC_SetJogParamsBlock(serial_number)

    return output


SCC_SetJogStepSize = lib.SCC_SetJogStepSize
SCC_SetJogStepSize.restype = c_short
SCC_SetJogStepSize.argtypes = []


def set_jog_step_size(serial_number):
    '''
    Sets the distance to move on jogging.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepSize: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepSize = c_uint()

    output = SCC_SetJogStepSize(serial_number)

    return output


SCC_SetJogVelParams = lib.SCC_SetJogVelParams
SCC_SetJogVelParams.restype = c_short
SCC_SetJogVelParams.argtypes = []


def set_jog_vel_params(serial_number):
    '''
    Sets jog velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_SetJogVelParams(serial_number)

    return output


SCC_SetLEDswitches = lib.SCC_SetLEDswitches
SCC_SetLEDswitches.restype = c_short
SCC_SetLEDswitches.argtypes = []


def set_l_e_dswitches(serial_number):
    '''
    Set the LED indicator bits on cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        LEDswitches: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    LEDswitches = c_long()

    output = SCC_SetLEDswitches(serial_number)

    return output


SCC_SetLimitSwitchParams = lib.SCC_SetLimitSwitchParams
SCC_SetLimitSwitchParams.restype = c_short
SCC_SetLimitSwitchParams.argtypes = []


def set_limit_switch_params(serial_number):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
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
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = SCC_SetLimitSwitchParams(serial_number)

    return output


SCC_SetLimitSwitchParamsBlock = lib.SCC_SetLimitSwitchParamsBlock
SCC_SetLimitSwitchParamsBlock.restype = c_short
SCC_SetLimitSwitchParamsBlock.argtypes = []


def set_limit_switch_params_block(serial_number):
    '''
    Set the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        limitSwitchParams: MOT_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = SCC_SetLimitSwitchParamsBlock(serial_number)

    return output


SCC_SetLimitsSoftwareApproachPolicy = lib.SCC_SetLimitsSoftwareApproachPolicy
SCC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
SCC_SetLimitsSoftwareApproachPolicy.argtypes = []


def set_limits_software_approach_policy(serial_number):
    '''
    Sets the software limits mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        limitsSoftwareApproachPolicy: MOT_LimitsSoftwareApproachPolicy

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = SCC_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


SCC_SetMotorParams = lib.SCC_SetMotorParams
SCC_SetMotorParams.restype = c_short
SCC_SetMotorParams.argtypes = []


def set_motor_params(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_long
        gearBoxRatio: c_long
        pitch: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = SCC_SetMotorParams(serial_number)

    return output


SCC_SetMotorParamsExt = lib.SCC_SetMotorParamsExt
SCC_SetMotorParamsExt.restype = c_short
SCC_SetMotorParamsExt.argtypes = []


def set_motor_params_ext(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_double
        gearBoxRatio: c_double
        pitch: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = SCC_SetMotorParamsExt(serial_number)

    return output


SCC_SetMotorTravelLimits = lib.SCC_SetMotorTravelLimits
SCC_SetMotorTravelLimits.restype = c_short
SCC_SetMotorTravelLimits.argtypes = []


def set_motor_travel_limits(serial_number):
    '''
    Sets the absolute minimum and maximum travel range constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        minPosition: c_double
        maxPosition: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    minPosition = c_double()
    maxPosition = c_double()

    output = SCC_SetMotorTravelLimits(serial_number)

    return output


SCC_SetMotorTravelMode = lib.SCC_SetMotorTravelMode
SCC_SetMotorTravelMode.restype = c_short
SCC_SetMotorTravelMode.argtypes = []


def set_motor_travel_mode(serial_number):
    '''
    Set the motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        travelMode: MOT_TravelModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    travelMode = MOT_TravelModes()

    output = SCC_SetMotorTravelMode(serial_number)

    return output


SCC_SetMotorVelocityLimits = lib.SCC_SetMotorVelocityLimits
SCC_SetMotorVelocityLimits.restype = c_short
SCC_SetMotorVelocityLimits.argtypes = []


def set_motor_velocity_limits(serial_number):
    '''
    Sets the absolute maximum velocity and acceleration constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxVelocity: c_double
        maxAcceleration: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = SCC_SetMotorVelocityLimits(serial_number)

    return output


SCC_SetMoveAbsolutePosition = lib.SCC_SetMoveAbsolutePosition
SCC_SetMoveAbsolutePosition.restype = c_short
SCC_SetMoveAbsolutePosition.argtypes = []


def set_move_absolute_position(serial_number):
    '''
    Sets the move absolute position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    position = c_int()

    output = SCC_SetMoveAbsolutePosition(serial_number)

    return output


SCC_SetMoveRelativeDistance = lib.SCC_SetMoveRelativeDistance
SCC_SetMoveRelativeDistance.restype = c_short
SCC_SetMoveRelativeDistance.argtypes = []


def set_move_relative_distance(serial_number):
    '''
    Sets the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        distance: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    distance = c_int()

    output = SCC_SetMoveRelativeDistance(serial_number)

    return output


SCC_SetPositionCounter = lib.SCC_SetPositionCounter
SCC_SetPositionCounter.restype = c_short
SCC_SetPositionCounter.argtypes = []


def set_position_counter(serial_number):
    '''
    Set the Position Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        count: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    count = c_long()

    output = SCC_SetPositionCounter(serial_number)

    return output


SCC_SetPotentiometerParams = lib.SCC_SetPotentiometerParams
SCC_SetPotentiometerParams.restype = c_short
SCC_SetPotentiometerParams.argtypes = []


def set_potentiometer_params(serial_number):
    '''
    Sets the potentiometer parameters for the TCube.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_short
        thresholdDeflection: c_long
        velocity: c_ulong

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = SCC_SetPotentiometerParams(serial_number)

    return output


SCC_SetPotentiometerParamsBlock = lib.SCC_SetPotentiometerParamsBlock
SCC_SetPotentiometerParamsBlock.restype = c_short
SCC_SetPotentiometerParamsBlock.argtypes = []


def set_potentiometer_params_block(serial_number):
    '''
    Set the potentiometer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        potentiometerSteps: MOT_PotentiometerSteps

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = SCC_SetPotentiometerParamsBlock(serial_number)

    return output


SCC_SetPowerParams = lib.SCC_SetPowerParams
SCC_SetPowerParams.restype = c_short
SCC_SetPowerParams.argtypes = []


def set_power_params(serial_number):
    '''
    Sets the power parameters for the stepper motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        powerParams: MOT_PowerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    powerParams = MOT_PowerParameters()

    output = SCC_SetPowerParams(serial_number)

    return output


SCC_SetRotationModes = lib.SCC_SetRotationModes
SCC_SetRotationModes.restype = c_short
SCC_SetRotationModes.argtypes = []


def set_rotation_modes(serial_number):
    '''
    Set the rotation modes for a rotational device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: MOT_MovementModes
        direction: MOT_MovementDirections

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = SCC_SetRotationModes(serial_number)

    return output


SCC_SetStageAxisLimits = lib.SCC_SetStageAxisLimits
SCC_SetStageAxisLimits.restype = c_short
SCC_SetStageAxisLimits.argtypes = []


def set_stage_axis_limits(serial_number):
    '''
    Sets the stage axis position limits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        minPosition: c_int
        maxPosition: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    minPosition = c_int()
    maxPosition = c_int()

    output = SCC_SetStageAxisLimits(serial_number)

    return output


SCC_SetStageType = lib.SCC_SetStageType
SCC_SetStageType.restype = c_short
SCC_SetStageType.argtypes = []


def set_stage_type(serial_number):
    '''
    Sets the stage type.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stageId: KST_Stages
        stageId: TST_Stages

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stageId = KST_Stages()
    stageId = TST_Stages()

    output = SCC_SetStageType(serial_number)

    return output


SCC_SetVelParams = lib.SCC_SetVelParams
SCC_SetVelParams.restype = c_short
SCC_SetVelParams.argtypes = []


def set_vel_params(serial_number):
    '''
    Sets the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = SCC_SetVelParams(serial_number)

    return output


SCC_SetVelParamsBlock = lib.SCC_SetVelParamsBlock
SCC_SetVelParamsBlock.restype = c_short
SCC_SetVelParamsBlock.argtypes = []


def set_vel_params_block(serial_number):
    '''
    Set the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocityParams: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocityParams = MOT_VelocityParameters()

    output = SCC_SetVelParamsBlock(serial_number)

    return output


SCC_StartPolling = lib.SCC_StartPolling
SCC_StartPolling.restype = c_bool
SCC_StartPolling.argtypes = []


def start_polling(serial_number):
    '''
    Starts the internal polling loop which continuously requests position and status.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        milliseconds: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    milliseconds = c_int()

    output = SCC_StartPolling(serial_number)

    return output


SCC_StopImmediate = lib.SCC_StopImmediate
SCC_StopImmediate.restype = c_short
SCC_StopImmediate.argtypes = []


def stop_immediate(serial_number):
    '''
    Stop the current move immediately (with risk of losing track of position).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_StopImmediate(serial_number)

    return output


SCC_StopPolling = lib.SCC_StopPolling
SCC_StopPolling.restype = c_void_p
SCC_StopPolling.argtypes = []


def stop_polling(serial_number):
    '''
    Stops the internal polling loop.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_StopPolling(serial_number)

    return output


SCC_StopProfiled = lib.SCC_StopProfiled
SCC_StopProfiled.restype = c_short
SCC_StopProfiled.argtypes = []


def stop_profiled(serial_number):
    '''
    Stop the current move using the current velocity profile.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_StopProfiled(serial_number)

    return output


SCC_SuspendMoveMessages = lib.SCC_SuspendMoveMessages
SCC_SuspendMoveMessages.restype = c_short
SCC_SuspendMoveMessages.argtypes = []


def suspend_move_messages(serial_number):
    '''
    Suspend automatic messages at ends of moves.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SCC_SuspendMoveMessages(serial_number)

    return output


SCC_TimeSinceLastMsgReceived = lib.SCC_TimeSinceLastMsgReceived
SCC_TimeSinceLastMsgReceived.restype = c_bool
SCC_TimeSinceLastMsgReceived.argtypes = []


def time_since_last_msg_received(serial_number):
    '''
    Gets the time in milliseconds since tha last message was received from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        lastUpdateTimeMS: c_int64

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    lastUpdateTimeMS = c_int64()

    output = SCC_TimeSinceLastMsgReceived(serial_number)

    return output


SCC_WaitForMessage = lib.SCC_WaitForMessage
SCC_WaitForMessage.restype = c_bool
SCC_WaitForMessage.argtypes = []


def wait_for_message(serial_number):
    '''
    Wait for next MessageQueue item.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SCC_WaitForMessage(serial_number)

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
TLI_GetDeviceInfo.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    serialNumber = POINTER(c_char)()
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = []


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
TLI_GetDeviceListByType.argtypes = []


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

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = []


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

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = []


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

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = []


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

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = []


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

    if output != 0:
        raise KinesisException(output)



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

    if output != 0:
        raise KinesisException(output)



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


