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
    '''
    Can the device perform a Home.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_CanHome(serial_number)

    return output


CC_CanMoveWithoutHomingFirst = lib.CC_CanMoveWithoutHomingFirst
CC_CanMoveWithoutHomingFirst.restype = c_bool
CC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_CanMoveWithoutHomingFirst(serial_number)

    return output


CC_CheckConnection = lib.CC_CheckConnection
CC_CheckConnection.restype = c_bool
CC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = CC_CheckConnection(serial_number)

    return output


CC_ClearMessageQueue = lib.CC_ClearMessageQueue
CC_ClearMessageQueue.restype = c_void_p
CC_ClearMessageQueue.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_ClearMessageQueue(serial_number)

    return output


CC_Close = lib.CC_Close
CC_Close.restype = c_void_p
CC_Close.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_Close(serial_number)

    return output


CC_DisableChannel = lib.CC_DisableChannel
CC_DisableChannel.restype = c_short
CC_DisableChannel.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_DisableChannel(serial_number)

    return output


CC_EnableChannel = lib.CC_EnableChannel
CC_EnableChannel.restype = c_short
CC_EnableChannel.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_EnableChannel(serial_number)

    return output


CC_EnableLastMsgTimer = lib.CC_EnableLastMsgTimer
CC_EnableLastMsgTimer.restype = c_void_p
CC_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = CC_EnableLastMsgTimer(serial_number)

    return output


CC_GetBacklash = lib.CC_GetBacklash
CC_GetBacklash.restype = c_long
CC_GetBacklash.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetBacklash(serial_number)

    return output


CC_GetButtonParams = lib.CC_GetButtonParams
CC_GetButtonParams.restype = c_short
CC_GetButtonParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()
    timeout = c_short()

    output = CC_GetButtonParams(serial_number)

    return output


CC_GetButtonParamsBlock = lib.CC_GetButtonParamsBlock
CC_GetButtonParamsBlock.restype = c_short
CC_GetButtonParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    buttonParams = MOT_ButtonParameters()

    output = CC_GetButtonParamsBlock(serial_number)

    return output


CC_GetDCPIDParams = lib.CC_GetDCPIDParams
CC_GetDCPIDParams.restype = c_short
CC_GetDCPIDParams.argtypes = [POINTER(c_char)]


def get_d_c_p_i_d_params(serial_number):
    '''
    Get the DC PID parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        DCproportionalIntegralDerivativeParams: MOT_DC_PIDParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()

    output = CC_GetDCPIDParams(serial_number)

    return output


CC_GetDeviceUnitFromRealValue = lib.CC_GetDeviceUnitFromRealValue
CC_GetDeviceUnitFromRealValue.restype = c_short
CC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = CC_GetDeviceUnitFromRealValue(serial_number)

    return output


CC_GetEncoderCounter = lib.CC_GetEncoderCounter
CC_GetEncoderCounter.restype = c_long
CC_GetEncoderCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetEncoderCounter(serial_number)

    return output


CC_GetHardwareInfo = lib.CC_GetHardwareInfo
CC_GetHardwareInfo.restype = c_short
CC_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
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
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = CC_GetHardwareInfo(serial_number)

    return output


CC_GetHardwareInfoBlock = lib.CC_GetHardwareInfoBlock
CC_GetHardwareInfoBlock.restype = c_short
CC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        hardwareInfo: TLI_HardwareInformation

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hardwareInfo = TLI_HardwareInformation()

    output = CC_GetHardwareInfoBlock(serial_number)

    return output


CC_GetHomingParamsBlock = lib.CC_GetHomingParamsBlock
CC_GetHomingParamsBlock.restype = c_short
CC_GetHomingParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    homingParams = MOT_HomingParameters()

    output = CC_GetHomingParamsBlock(serial_number)

    return output


CC_GetHomingVelocity = lib.CC_GetHomingVelocity
CC_GetHomingVelocity.restype = c_uint
CC_GetHomingVelocity.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetHomingVelocity(serial_number)

    return output


CC_GetHubBay = lib.CC_GetHubBay
CC_GetHubBay.restype = POINTER(c_char)
CC_GetHubBay.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetHubBay(serial_number)

    return output


CC_GetJogMode = lib.CC_GetJogMode
CC_GetJogMode.restype = c_short
CC_GetJogMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = CC_GetJogMode(serial_number)

    return output


CC_GetJogParamsBlock = lib.CC_GetJogParamsBlock
CC_GetJogParamsBlock.restype = c_short
CC_GetJogParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    jogParams = MOT_JogParameters()

    output = CC_GetJogParamsBlock(serial_number)

    return output


CC_GetJogStepSize = lib.CC_GetJogStepSize
CC_GetJogStepSize.restype = c_uint
CC_GetJogStepSize.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetJogStepSize(serial_number)

    return output


CC_GetJogVelParams = lib.CC_GetJogVelParams
CC_GetJogVelParams.restype = c_short
CC_GetJogVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_GetJogVelParams(serial_number)

    return output


CC_GetLEDswitches = lib.CC_GetLEDswitches
CC_GetLEDswitches.restype = c_long
CC_GetLEDswitches.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetLEDswitches(serial_number)

    return output


CC_GetLimitSwitchParams = lib.CC_GetLimitSwitchParams
CC_GetLimitSwitchParams.restype = c_short
CC_GetLimitSwitchParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = CC_GetLimitSwitchParams(serial_number)

    return output


CC_GetLimitSwitchParamsBlock = lib.CC_GetLimitSwitchParamsBlock
CC_GetLimitSwitchParamsBlock.restype = c_short
CC_GetLimitSwitchParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = CC_GetLimitSwitchParamsBlock(serial_number)

    return output


CC_GetMotorParams = lib.CC_GetMotorParams
CC_GetMotorParams.restype = c_short
CC_GetMotorParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = CC_GetMotorParams(serial_number)

    return output


CC_GetMotorParamsExt = lib.CC_GetMotorParamsExt
CC_GetMotorParamsExt.restype = c_short
CC_GetMotorParamsExt.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = CC_GetMotorParamsExt(serial_number)

    return output


CC_GetMotorTravelLimits = lib.CC_GetMotorTravelLimits
CC_GetMotorTravelLimits.restype = c_short
CC_GetMotorTravelLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    minPosition = c_double()
    maxPosition = c_double()

    output = CC_GetMotorTravelLimits(serial_number)

    return output


CC_GetMotorTravelMode = lib.CC_GetMotorTravelMode
CC_GetMotorTravelMode.restype = MOT_TravelModes
CC_GetMotorTravelMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetMotorTravelMode(serial_number)

    return output


CC_GetMotorVelocityLimits = lib.CC_GetMotorVelocityLimits
CC_GetMotorVelocityLimits.restype = c_short
CC_GetMotorVelocityLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = CC_GetMotorVelocityLimits(serial_number)

    return output


CC_GetMoveAbsolutePosition = lib.CC_GetMoveAbsolutePosition
CC_GetMoveAbsolutePosition.restype = c_int
CC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetMoveAbsolutePosition(serial_number)

    return output


CC_GetMoveRelativeDistance = lib.CC_GetMoveRelativeDistance
CC_GetMoveRelativeDistance.restype = c_int
CC_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetMoveRelativeDistance(serial_number)

    return output


CC_GetNextMessage = lib.CC_GetNextMessage
CC_GetNextMessage.restype = c_bool
CC_GetNextMessage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = CC_GetNextMessage(serial_number)

    return output


CC_GetNumberPositions = lib.CC_GetNumberPositions
CC_GetNumberPositions.restype = c_int
CC_GetNumberPositions.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetNumberPositions(serial_number)

    return output


CC_GetPosition = lib.CC_GetPosition
CC_GetPosition.restype = c_int
CC_GetPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetPosition(serial_number)

    return output


CC_GetPositionCounter = lib.CC_GetPositionCounter
CC_GetPositionCounter.restype = c_long
CC_GetPositionCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetPositionCounter(serial_number)

    return output


CC_GetPotentiometerParams = lib.CC_GetPotentiometerParams
CC_GetPotentiometerParams.restype = c_short
CC_GetPotentiometerParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = CC_GetPotentiometerParams(serial_number)

    return output


CC_GetPotentiometerParamsBlock = lib.CC_GetPotentiometerParamsBlock
CC_GetPotentiometerParamsBlock.restype = c_short
CC_GetPotentiometerParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    potentiometerSteps = MOT_PotentiometerSteps()

    output = CC_GetPotentiometerParamsBlock(serial_number)

    return output


CC_GetRealValueFromDeviceUnit = lib.CC_GetRealValueFromDeviceUnit
CC_GetRealValueFromDeviceUnit.restype = c_short
CC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = CC_GetRealValueFromDeviceUnit(serial_number)

    return output


CC_GetSoftLimitMode = lib.CC_GetSoftLimitMode
CC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
CC_GetSoftLimitMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetSoftLimitMode(serial_number)

    return output


CC_GetSoftwareVersion = lib.CC_GetSoftwareVersion
CC_GetSoftwareVersion.restype = c_ulong
CC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = CC_GetSoftwareVersion(serial_number)

    return output


CC_GetStageAxisMaxPos = lib.CC_GetStageAxisMaxPos
CC_GetStageAxisMaxPos.restype = c_int
CC_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


def get_stage_axis_max_pos(serial_number):
    '''
    Gets the DC Motor maximum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetStageAxisMaxPos(serial_number)

    return output


CC_GetStageAxisMinPos = lib.CC_GetStageAxisMinPos
CC_GetStageAxisMinPos.restype = c_int
CC_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


def get_stage_axis_min_pos(serial_number):
    '''
    Gets the DC Motor minimum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetStageAxisMinPos(serial_number)

    return output


CC_GetStatusBits = lib.CC_GetStatusBits
CC_GetStatusBits.restype = c_ulong
CC_GetStatusBits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_GetStatusBits(serial_number)

    return output


CC_GetVelParams = lib.CC_GetVelParams
CC_GetVelParams.restype = c_short
CC_GetVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_GetVelParams(serial_number)

    return output


CC_GetVelParamsBlock = lib.CC_GetVelParamsBlock
CC_GetVelParamsBlock.restype = c_short
CC_GetVelParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    velocityParams = MOT_VelocityParameters()

    output = CC_GetVelParamsBlock(serial_number)

    return output


CC_HasLastMsgTimerOverrun = lib.CC_HasLastMsgTimerOverrun
CC_HasLastMsgTimerOverrun.restype = c_bool
CC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by CC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_HasLastMsgTimerOverrun(serial_number)

    return output


CC_Home = lib.CC_Home
CC_Home.restype = c_short
CC_Home.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_Home(serial_number)

    return output


CC_Identify = lib.CC_Identify
CC_Identify.restype = c_void_p
CC_Identify.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_Identify(serial_number)

    return output


CC_LoadNamedSettings = lib.CC_LoadNamedSettings
CC_LoadNamedSettings.restype = c_bool
CC_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    settingsName = POINTER(c_char)()

    output = CC_LoadNamedSettings(serial_number)

    return output


CC_LoadSettings = lib.CC_LoadSettings
CC_LoadSettings.restype = c_bool
CC_LoadSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_LoadSettings(serial_number)

    return output


CC_MessageQueueSize = lib.CC_MessageQueueSize
CC_MessageQueueSize.restype = c_int
CC_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_MessageQueueSize(serial_number)

    return output


CC_MoveAbsolute = lib.CC_MoveAbsolute
CC_MoveAbsolute.restype = c_short
CC_MoveAbsolute.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_MoveAbsolute(serial_number)

    return output


CC_MoveAtVelocity = lib.CC_MoveAtVelocity
CC_MoveAtVelocity.restype = c_short
CC_MoveAtVelocity.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    direction = MOT_TravelDirection()

    output = CC_MoveAtVelocity(serial_number)

    return output


CC_MoveJog = lib.CC_MoveJog
CC_MoveJog.restype = c_short
CC_MoveJog.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    jogDirection = MOT_TravelDirection()

    output = CC_MoveJog(serial_number)

    return output


CC_MoveRelative = lib.CC_MoveRelative
CC_MoveRelative.restype = c_short
CC_MoveRelative.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    displacement = c_int()

    output = CC_MoveRelative(serial_number)

    return output


CC_MoveRelativeDistance = lib.CC_MoveRelativeDistance
CC_MoveRelativeDistance.restype = c_short
CC_MoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_MoveRelativeDistance(serial_number)

    return output


CC_MoveToPosition = lib.CC_MoveToPosition
CC_MoveToPosition.restype = c_short
CC_MoveToPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    index = c_int()

    output = CC_MoveToPosition(serial_number)

    return output


CC_NeedsHoming = lib.CC_NeedsHoming
CC_NeedsHoming.restype = c_bool
CC_NeedsHoming.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_NeedsHoming(serial_number)

    return output


CC_Open = lib.CC_Open
CC_Open.restype = c_short
CC_Open.argtypes = [POINTER(c_char)]


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

    output = CC_Open(serial_number)

    return output


CC_PersistSettings = lib.CC_PersistSettings
CC_PersistSettings.restype = c_bool
CC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_PersistSettings(serial_number)

    return output


CC_PollingDuration = lib.CC_PollingDuration
CC_PollingDuration.restype = c_long
CC_PollingDuration.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_PollingDuration(serial_number)

    return output


CC_RegisterMessageCallback = lib.CC_RegisterMessageCallback
CC_RegisterMessageCallback.restype = c_void_p
CC_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RegisterMessageCallback(serial_number)

    return output


CC_RequestBacklash = lib.CC_RequestBacklash
CC_RequestBacklash.restype = c_short
CC_RequestBacklash.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestBacklash(serial_number)

    return output


CC_RequestButtonParams = lib.CC_RequestButtonParams
CC_RequestButtonParams.restype = c_short
CC_RequestButtonParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestButtonParams(serial_number)

    return output


CC_RequestDCPIDParams = lib.CC_RequestDCPIDParams
CC_RequestDCPIDParams.restype = c_short
CC_RequestDCPIDParams.argtypes = [POINTER(c_char)]


def request_d_c_p_i_d_params(serial_number):
    '''
    Requests the PID parameters for DC motors used in an algorithm involving calculus.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestDCPIDParams(serial_number)

    return output


CC_RequestEncoderCounter = lib.CC_RequestEncoderCounter
CC_RequestEncoderCounter.restype = c_short
CC_RequestEncoderCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestEncoderCounter(serial_number)

    return output


CC_RequestHomingParams = lib.CC_RequestHomingParams
CC_RequestHomingParams.restype = c_short
CC_RequestHomingParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestHomingParams(serial_number)

    return output


CC_RequestJogParams = lib.CC_RequestJogParams
CC_RequestJogParams.restype = c_short
CC_RequestJogParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestJogParams(serial_number)

    return output


CC_RequestLEDswitches = lib.CC_RequestLEDswitches
CC_RequestLEDswitches.restype = c_short
CC_RequestLEDswitches.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestLEDswitches(serial_number)

    return output


CC_RequestLimitSwitchParams = lib.CC_RequestLimitSwitchParams
CC_RequestLimitSwitchParams.restype = c_short
CC_RequestLimitSwitchParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestLimitSwitchParams(serial_number)

    return output


CC_RequestMoveAbsolutePosition = lib.CC_RequestMoveAbsolutePosition
CC_RequestMoveAbsolutePosition.restype = c_short
CC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestMoveAbsolutePosition(serial_number)

    return output


CC_RequestMoveRelativeDistance = lib.CC_RequestMoveRelativeDistance
CC_RequestMoveRelativeDistance.restype = c_short
CC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


def request_move_relative_distance(serial_number):
    '''
    Requests the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestMoveRelativeDistance(serial_number)

    return output


CC_RequestPosition = lib.CC_RequestPosition
CC_RequestPosition.restype = c_short
CC_RequestPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestPosition(serial_number)

    return output


CC_RequestPotentiometerParams = lib.CC_RequestPotentiometerParams
CC_RequestPotentiometerParams.restype = c_short
CC_RequestPotentiometerParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestPotentiometerParams(serial_number)

    return output


CC_RequestSettings = lib.CC_RequestSettings
CC_RequestSettings.restype = c_short
CC_RequestSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestSettings(serial_number)

    return output


CC_RequestStatusBits = lib.CC_RequestStatusBits
CC_RequestStatusBits.restype = c_short
CC_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestStatusBits(serial_number)

    return output


CC_RequestVelParams = lib.CC_RequestVelParams
CC_RequestVelParams.restype = c_short
CC_RequestVelParams.argtypes = [POINTER(c_char)]


def request_vel_params(serial_number):
    '''
    Requests the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_RequestVelParams(serial_number)

    return output


CC_ResetRotationModes = lib.CC_ResetRotationModes
CC_ResetRotationModes.restype = c_short
CC_ResetRotationModes.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_ResetRotationModes(serial_number)

    return output


CC_ResumeMoveMessages = lib.CC_ResumeMoveMessages
CC_ResumeMoveMessages.restype = c_short
CC_ResumeMoveMessages.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_ResumeMoveMessages(serial_number)

    return output


CC_SetBacklash = lib.CC_SetBacklash
CC_SetBacklash.restype = c_short
CC_SetBacklash.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    distance = c_long()

    output = CC_SetBacklash(serial_number)

    return output


CC_SetButtonParams = lib.CC_SetButtonParams
CC_SetButtonParams.restype = c_short
CC_SetButtonParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()

    output = CC_SetButtonParams(serial_number)

    return output


CC_SetButtonParamsBlock = lib.CC_SetButtonParamsBlock
CC_SetButtonParamsBlock.restype = c_short
CC_SetButtonParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    buttonParams = MOT_ButtonParameters()

    output = CC_SetButtonParamsBlock(serial_number)

    return output


CC_SetDCPIDParams = lib.CC_SetDCPIDParams
CC_SetDCPIDParams.restype = c_short
CC_SetDCPIDParams.argtypes = [POINTER(c_char)]


def set_d_c_p_i_d_params(serial_number):
    '''
    Set the PID parameters for DC motors used in an algorithm involving calculus.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        DCproportionalIntegralDerivativeParams: MOT_DC_PIDParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    DCproportionalIntegralDerivativeParams = MOT_DC_PIDParameters()

    output = CC_SetDCPIDParams(serial_number)

    return output


CC_SetDirection = lib.CC_SetDirection
CC_SetDirection.restype = c_void_p
CC_SetDirection.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    reverse = c_bool()

    output = CC_SetDirection(serial_number)

    return output


CC_SetEncoderCounter = lib.CC_SetEncoderCounter
CC_SetEncoderCounter.restype = c_short
CC_SetEncoderCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    count = c_long()

    output = CC_SetEncoderCounter(serial_number)

    return output


CC_SetHomingParamsBlock = lib.CC_SetHomingParamsBlock
CC_SetHomingParamsBlock.restype = c_short
CC_SetHomingParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    homingParams = MOT_HomingParameters()

    output = CC_SetHomingParamsBlock(serial_number)

    return output


CC_SetHomingVelocity = lib.CC_SetHomingVelocity
CC_SetHomingVelocity.restype = c_short
CC_SetHomingVelocity.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    velocity = c_uint()

    output = CC_SetHomingVelocity(serial_number)

    return output


CC_SetJogMode = lib.CC_SetJogMode
CC_SetJogMode.restype = c_short
CC_SetJogMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = CC_SetJogMode(serial_number)

    return output


CC_SetJogParamsBlock = lib.CC_SetJogParamsBlock
CC_SetJogParamsBlock.restype = c_short
CC_SetJogParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    jogParams = MOT_JogParameters()

    output = CC_SetJogParamsBlock(serial_number)

    return output


CC_SetJogStepSize = lib.CC_SetJogStepSize
CC_SetJogStepSize.restype = c_short
CC_SetJogStepSize.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    stepSize = c_uint()

    output = CC_SetJogStepSize(serial_number)

    return output


CC_SetJogVelParams = lib.CC_SetJogVelParams
CC_SetJogVelParams.restype = c_short
CC_SetJogVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_SetJogVelParams(serial_number)

    return output


CC_SetLEDswitches = lib.CC_SetLEDswitches
CC_SetLEDswitches.restype = c_short
CC_SetLEDswitches.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    LEDswitches = c_long()

    output = CC_SetLEDswitches(serial_number)

    return output


CC_SetLimitSwitchParams = lib.CC_SetLimitSwitchParams
CC_SetLimitSwitchParams.restype = c_short
CC_SetLimitSwitchParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = CC_SetLimitSwitchParams(serial_number)

    return output


CC_SetLimitSwitchParamsBlock = lib.CC_SetLimitSwitchParamsBlock
CC_SetLimitSwitchParamsBlock.restype = c_short
CC_SetLimitSwitchParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = CC_SetLimitSwitchParamsBlock(serial_number)

    return output


CC_SetLimitsSoftwareApproachPolicy = lib.CC_SetLimitsSoftwareApproachPolicy
CC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
CC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = CC_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


CC_SetMotorParams = lib.CC_SetMotorParams
CC_SetMotorParams.restype = c_short
CC_SetMotorParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = CC_SetMotorParams(serial_number)

    return output


CC_SetMotorParamsExt = lib.CC_SetMotorParamsExt
CC_SetMotorParamsExt.restype = c_short
CC_SetMotorParamsExt.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = CC_SetMotorParamsExt(serial_number)

    return output


CC_SetMotorTravelLimits = lib.CC_SetMotorTravelLimits
CC_SetMotorTravelLimits.restype = c_short
CC_SetMotorTravelLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    minPosition = c_double()
    maxPosition = c_double()

    output = CC_SetMotorTravelLimits(serial_number)

    return output


CC_SetMotorTravelMode = lib.CC_SetMotorTravelMode
CC_SetMotorTravelMode.restype = c_short
CC_SetMotorTravelMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    travelMode = MOT_TravelModes()

    output = CC_SetMotorTravelMode(serial_number)

    return output


CC_SetMotorVelocityLimits = lib.CC_SetMotorVelocityLimits
CC_SetMotorVelocityLimits.restype = c_short
CC_SetMotorVelocityLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = CC_SetMotorVelocityLimits(serial_number)

    return output


CC_SetMoveAbsolutePosition = lib.CC_SetMoveAbsolutePosition
CC_SetMoveAbsolutePosition.restype = c_short
CC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_int()

    output = CC_SetMoveAbsolutePosition(serial_number)

    return output


CC_SetMoveRelativeDistance = lib.CC_SetMoveRelativeDistance
CC_SetMoveRelativeDistance.restype = c_short
CC_SetMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    distance = c_int()

    output = CC_SetMoveRelativeDistance(serial_number)

    return output


CC_SetPositionCounter = lib.CC_SetPositionCounter
CC_SetPositionCounter.restype = c_short
CC_SetPositionCounter.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    count = c_long()

    output = CC_SetPositionCounter(serial_number)

    return output


CC_SetPotentiometerParams = lib.CC_SetPotentiometerParams
CC_SetPotentiometerParams.restype = c_short
CC_SetPotentiometerParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = CC_SetPotentiometerParams(serial_number)

    return output


CC_SetPotentiometerParamsBlock = lib.CC_SetPotentiometerParamsBlock
CC_SetPotentiometerParamsBlock.restype = c_short
CC_SetPotentiometerParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    potentiometerSteps = MOT_PotentiometerSteps()

    output = CC_SetPotentiometerParamsBlock(serial_number)

    return output


CC_SetRotationModes = lib.CC_SetRotationModes
CC_SetRotationModes.restype = c_short
CC_SetRotationModes.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = CC_SetRotationModes(serial_number)

    return output


CC_SetStageAxisLimits = lib.CC_SetStageAxisLimits
CC_SetStageAxisLimits.restype = c_short
CC_SetStageAxisLimits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    minPosition = c_int()
    maxPosition = c_int()

    output = CC_SetStageAxisLimits(serial_number)

    return output


CC_SetVelParams = lib.CC_SetVelParams
CC_SetVelParams.restype = c_short
CC_SetVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    acceleration = c_int()
    maxVelocity = c_int()

    output = CC_SetVelParams(serial_number)

    return output


CC_SetVelParamsBlock = lib.CC_SetVelParamsBlock
CC_SetVelParamsBlock.restype = c_short
CC_SetVelParamsBlock.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    velocityParams = MOT_VelocityParameters()

    output = CC_SetVelParamsBlock(serial_number)

    return output


CC_StartPolling = lib.CC_StartPolling
CC_StartPolling.restype = c_bool
CC_StartPolling.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    milliseconds = c_int()

    output = CC_StartPolling(serial_number)

    return output


CC_StopImmediate = lib.CC_StopImmediate
CC_StopImmediate.restype = c_short
CC_StopImmediate.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_StopImmediate(serial_number)

    return output


CC_StopPolling = lib.CC_StopPolling
CC_StopPolling.restype = c_void_p
CC_StopPolling.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_StopPolling(serial_number)

    return output


CC_StopProfiled = lib.CC_StopProfiled
CC_StopProfiled.restype = c_short
CC_StopProfiled.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_StopProfiled(serial_number)

    return output


CC_SuspendMoveMessages = lib.CC_SuspendMoveMessages
CC_SuspendMoveMessages.restype = c_short
CC_SuspendMoveMessages.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = CC_SuspendMoveMessages(serial_number)

    return output


CC_TimeSinceLastMsgReceived = lib.CC_TimeSinceLastMsgReceived
CC_TimeSinceLastMsgReceived.restype = c_bool
CC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lastUpdateTimeMS = c_int64()

    output = CC_TimeSinceLastMsgReceived(serial_number)

    return output


CC_WaitForMessage = lib.CC_WaitForMessage
CC_WaitForMessage.restype = c_bool
CC_WaitForMessage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = CC_WaitForMessage(serial_number)

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


