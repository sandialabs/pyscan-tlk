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
    c_uint,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    MOT_JogModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    KMOT_TriggerConfig,
    KMOT_TriggerParams,
    MOT_BrushlessTrackSettleParameters,
    MOT_DC_PIDParameters,
    MOT_EncoderResolutionParams,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_VelocityParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.DCServo.dll")

KVS_CanDeviceLockFrontPanel = lib.KVS_CanDeviceLockFrontPanel
KVS_CanDeviceLockFrontPanel.restype = c_bool
KVS_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    '''
    Determine if the device front panel can be locked.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_CanDeviceLockFrontPanel(serial_number)

    return output


KVS_CanHome = lib.KVS_CanHome
KVS_CanHome.restype = c_bool
KVS_CanHome.argtypes = [POINTER(c_char)]


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

    output = KVS_CanHome(serial_number)

    return output


KVS_CanMoveWithoutHomingFirst = lib.KVS_CanMoveWithoutHomingFirst
KVS_CanMoveWithoutHomingFirst.restype = c_bool
KVS_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char)]


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

    output = KVS_CanMoveWithoutHomingFirst(serial_number)

    return output


KVS_CheckConnection = lib.KVS_CheckConnection
KVS_CheckConnection.restype = c_bool
KVS_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = KVS_CheckConnection(serial_number)

    return output


KVS_ClearMessageQueue = lib.KVS_ClearMessageQueue
KVS_ClearMessageQueue.restype = c_void_p
KVS_ClearMessageQueue.argtypes = [POINTER(c_char)]


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

    output = KVS_ClearMessageQueue(serial_number)

    return output


KVS_Close = lib.KVS_Close
KVS_Close.restype = c_void_p
KVS_Close.argtypes = [POINTER(c_char)]


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

    output = KVS_Close(serial_number)

    return output


KVS_DisableChannel = lib.KVS_DisableChannel
KVS_DisableChannel.restype = c_short
KVS_DisableChannel.argtypes = [POINTER(c_char)]


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

    output = KVS_DisableChannel(serial_number)

    return output


KVS_EnableChannel = lib.KVS_EnableChannel
KVS_EnableChannel.restype = c_short
KVS_EnableChannel.argtypes = [POINTER(c_char)]


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

    output = KVS_EnableChannel(serial_number)

    return output


KVS_EnableLastMsgTimer = lib.KVS_EnableLastMsgTimer
KVS_EnableLastMsgTimer.restype = c_void_p
KVS_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    output = KVS_EnableLastMsgTimer(serial_number)

    return output


KVS_GetBacklash = lib.KVS_GetBacklash
KVS_GetBacklash.restype = c_long
KVS_GetBacklash.argtypes = [POINTER(c_char)]


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

    output = KVS_GetBacklash(serial_number)

    return output


KVS_GetDCPIDParams = lib.KVS_GetDCPIDParams
KVS_GetDCPIDParams.restype = c_short
KVS_GetDCPIDParams.argtypes = [POINTER(c_char)]


def get_d_c_p_i_d_params(serial_number):
    '''
    Get the DC PID parameters for DC motors used in an algorithm involving calculus.

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

    output = KVS_GetDCPIDParams(serial_number)

    return output


KVS_GetDeviceUnitFromRealValue = lib.KVS_GetDeviceUnitFromRealValue
KVS_GetDeviceUnitFromRealValue.restype = c_short
KVS_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char)]


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

    output = KVS_GetDeviceUnitFromRealValue(serial_number)

    return output


KVS_GetDigitalOutputs = lib.KVS_GetDigitalOutputs
KVS_GetDigitalOutputs.restype = c_byte
KVS_GetDigitalOutputs.argtypes = [POINTER(c_char)]


def get_digital_outputs(serial_number):
    '''
    Gets the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_GetDigitalOutputs(serial_number)

    return output


KVS_GetEncoderCounter = lib.KVS_GetEncoderCounter
KVS_GetEncoderCounter.restype = c_long
KVS_GetEncoderCounter.argtypes = [POINTER(c_char)]


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

    output = KVS_GetEncoderCounter(serial_number)

    return output


KVS_GetEncoderResolutionParams = lib.KVS_GetEncoderResolutionParams
KVS_GetEncoderResolutionParams.restype = c_short
KVS_GetEncoderResolutionParams.argtypes = [POINTER(c_char)]


def get_encoder_resolution_params(serial_number):
    '''
    Get the encoder resolution parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        resolutionParams: MOT_EncoderResolutionParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    resolutionParams = MOT_EncoderResolutionParams()

    output = KVS_GetEncoderResolutionParams(serial_number)

    return output


KVS_GetFrontPanelLocked = lib.KVS_GetFrontPanelLocked
KVS_GetFrontPanelLocked.restype = c_bool
KVS_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    '''
    Query if the device front panel locked.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_GetFrontPanelLocked(serial_number)

    return output


KVS_GetHardwareInfo = lib.KVS_GetHardwareInfo
KVS_GetHardwareInfo.restype = c_short
KVS_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = KVS_GetHardwareInfo(serial_number)

    return output


KVS_GetHardwareInfoBlock = lib.KVS_GetHardwareInfoBlock
KVS_GetHardwareInfoBlock.restype = c_short
KVS_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_GetHardwareInfoBlock(serial_number)

    return output


KVS_GetHomingParamsBlock = lib.KVS_GetHomingParamsBlock
KVS_GetHomingParamsBlock.restype = c_short
KVS_GetHomingParamsBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_GetHomingParamsBlock(serial_number)

    return output


KVS_GetHomingVelocity = lib.KVS_GetHomingVelocity
KVS_GetHomingVelocity.restype = c_uint
KVS_GetHomingVelocity.argtypes = [POINTER(c_char)]


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

    output = KVS_GetHomingVelocity(serial_number)

    return output


KVS_GetHubBay = lib.KVS_GetHubBay
KVS_GetHubBay.restype = POINTER(c_char)
KVS_GetHubBay.argtypes = [POINTER(c_char)]


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

    output = KVS_GetHubBay(serial_number)

    return output


KVS_GetJogMode = lib.KVS_GetJogMode
KVS_GetJogMode.restype = c_short
KVS_GetJogMode.argtypes = [POINTER(c_char)]


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

    output = KVS_GetJogMode(serial_number)

    return output


KVS_GetJogParamsBlock = lib.KVS_GetJogParamsBlock
KVS_GetJogParamsBlock.restype = c_short
KVS_GetJogParamsBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_GetJogParamsBlock(serial_number)

    return output


KVS_GetJogStepSize = lib.KVS_GetJogStepSize
KVS_GetJogStepSize.restype = c_uint
KVS_GetJogStepSize.argtypes = [POINTER(c_char)]


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

    output = KVS_GetJogStepSize(serial_number)

    return output


KVS_GetJogVelParams = lib.KVS_GetJogVelParams
KVS_GetJogVelParams.restype = c_short
KVS_GetJogVelParams.argtypes = [POINTER(c_char)]


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

    output = KVS_GetJogVelParams(serial_number)

    return output


KVS_GetLEDswitches = lib.KVS_GetLEDswitches
KVS_GetLEDswitches.restype = c_long
KVS_GetLEDswitches.argtypes = [POINTER(c_char)]


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

    output = KVS_GetLEDswitches(serial_number)

    return output


KVS_GetMotorParams = lib.KVS_GetMotorParams
KVS_GetMotorParams.restype = c_short
KVS_GetMotorParams.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMotorParams(serial_number)

    return output


KVS_GetMotorParamsExt = lib.KVS_GetMotorParamsExt
KVS_GetMotorParamsExt.restype = c_short
KVS_GetMotorParamsExt.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMotorParamsExt(serial_number)

    return output


KVS_GetMotorTravelLimits = lib.KVS_GetMotorTravelLimits
KVS_GetMotorTravelLimits.restype = c_short
KVS_GetMotorTravelLimits.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMotorTravelLimits(serial_number)

    return output


KVS_GetMotorTravelMode = lib.KVS_GetMotorTravelMode
KVS_GetMotorTravelMode.restype = MOT_TravelModes
KVS_GetMotorTravelMode.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMotorTravelMode(serial_number)

    return output


KVS_GetMotorVelocityLimits = lib.KVS_GetMotorVelocityLimits
KVS_GetMotorVelocityLimits.restype = c_short
KVS_GetMotorVelocityLimits.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMotorVelocityLimits(serial_number)

    return output


KVS_GetMoveAbsolutePosition = lib.KVS_GetMoveAbsolutePosition
KVS_GetMoveAbsolutePosition.restype = c_int
KVS_GetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMoveAbsolutePosition(serial_number)

    return output


KVS_GetMoveRelativeDistance = lib.KVS_GetMoveRelativeDistance
KVS_GetMoveRelativeDistance.restype = c_int
KVS_GetMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    output = KVS_GetMoveRelativeDistance(serial_number)

    return output


KVS_GetNextMessage = lib.KVS_GetNextMessage
KVS_GetNextMessage.restype = c_bool
KVS_GetNextMessage.argtypes = [POINTER(c_char)]


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

    output = KVS_GetNextMessage(serial_number)

    return output


KVS_GetNumberPositions = lib.KVS_GetNumberPositions
KVS_GetNumberPositions.restype = c_int
KVS_GetNumberPositions.argtypes = [POINTER(c_char)]


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

    output = KVS_GetNumberPositions(serial_number)

    return output


KVS_GetPosition = lib.KVS_GetPosition
KVS_GetPosition.restype = c_int
KVS_GetPosition.argtypes = [POINTER(c_char)]


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

    output = KVS_GetPosition(serial_number)

    return output


KVS_GetPositionCounter = lib.KVS_GetPositionCounter
KVS_GetPositionCounter.restype = c_long
KVS_GetPositionCounter.argtypes = [POINTER(c_char)]


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

    output = KVS_GetPositionCounter(serial_number)

    return output


KVS_GetRealValueFromDeviceUnit = lib.KVS_GetRealValueFromDeviceUnit
KVS_GetRealValueFromDeviceUnit.restype = c_short
KVS_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char)]


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

    output = KVS_GetRealValueFromDeviceUnit(serial_number)

    return output


KVS_GetSoftLimitMode = lib.KVS_GetSoftLimitMode
KVS_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
KVS_GetSoftLimitMode.argtypes = [POINTER(c_char)]


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

    output = KVS_GetSoftLimitMode(serial_number)

    return output


KVS_GetSoftwareVersion = lib.KVS_GetSoftwareVersion
KVS_GetSoftwareVersion.restype = c_ulong
KVS_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = KVS_GetSoftwareVersion(serial_number)

    return output


KVS_GetStageAxisMaxPos = lib.KVS_GetStageAxisMaxPos
KVS_GetStageAxisMaxPos.restype = c_int
KVS_GetStageAxisMaxPos.argtypes = [POINTER(c_char)]


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

    output = KVS_GetStageAxisMaxPos(serial_number)

    return output


KVS_GetStageAxisMinPos = lib.KVS_GetStageAxisMinPos
KVS_GetStageAxisMinPos.restype = c_int
KVS_GetStageAxisMinPos.argtypes = [POINTER(c_char)]


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

    output = KVS_GetStageAxisMinPos(serial_number)

    return output


KVS_GetStatusBits = lib.KVS_GetStatusBits
KVS_GetStatusBits.restype = c_ulong
KVS_GetStatusBits.argtypes = [POINTER(c_char)]


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

    output = KVS_GetStatusBits(serial_number)

    return output


KVS_GetTrackSettleParams = lib.KVS_GetTrackSettleParams
KVS_GetTrackSettleParams.restype = c_short
KVS_GetTrackSettleParams.argtypes = [POINTER(c_char)]


def get_track_settle_params(serial_number):
    '''
    Gets the track settled parameters used to decide when settled at right position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        settleParams: MOT_BrushlessTrackSettleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    settleParams = MOT_BrushlessTrackSettleParameters()

    output = KVS_GetTrackSettleParams(serial_number)

    return output


KVS_GetTriggerConfigParams = lib.KVS_GetTriggerConfigParams
KVS_GetTriggerConfigParams.restype = c_short
KVS_GetTriggerConfigParams.argtypes = [POINTER(c_char)]


def get_trigger_config_params(serial_number):
    '''
    Get the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KMOT_TriggerPortMode
        trigger1Polarity: KMOT_TriggerPortPolarity
        trigger2Mode: KMOT_TriggerPortMode
        trigger2Polarity: KMOT_TriggerPortPolarity

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = KVS_GetTriggerConfigParams(serial_number)

    return output


KVS_GetTriggerConfigParamsBlock = lib.KVS_GetTriggerConfigParamsBlock
KVS_GetTriggerConfigParamsBlock.restype = c_short
KVS_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char)]


def get_trigger_config_params_block(serial_number):
    '''
    Gets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KMOT_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerConfigParams = KMOT_TriggerConfig()

    output = KVS_GetTriggerConfigParamsBlock(serial_number)

    return output


KVS_GetTriggerParamsParams = lib.KVS_GetTriggerParamsParams
KVS_GetTriggerParamsParams.restype = c_short
KVS_GetTriggerParamsParams.argtypes = [POINTER(c_char)]


def get_trigger_params_params(serial_number):
    '''
    Get the Trigger Parameters Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerStartPositionFwd: c_int32
        triggerIntervalFwd: c_int32
        triggerPulseCountFwd: c_int32
        triggerStartPositionRev: c_int32
        triggerIntervalRev: c_int32
        triggerPulseCountRev: c_int32
        triggerPulseWidth: c_int32
        cycleCount: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = KVS_GetTriggerParamsParams(serial_number)

    return output


KVS_GetTriggerParamsParamsBlock = lib.KVS_GetTriggerParamsParamsBlock
KVS_GetTriggerParamsParamsBlock.restype = c_short
KVS_GetTriggerParamsParamsBlock.argtypes = [POINTER(c_char)]


def get_trigger_params_params_block(serial_number):
    '''
    Gets the trigger parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerParamsParams: KMOT_TriggerParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerParamsParams = KMOT_TriggerParams()

    output = KVS_GetTriggerParamsParamsBlock(serial_number)

    return output


KVS_GetVelParams = lib.KVS_GetVelParams
KVS_GetVelParams.restype = c_short
KVS_GetVelParams.argtypes = [POINTER(c_char)]


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

    output = KVS_GetVelParams(serial_number)

    return output


KVS_GetVelParamsBlock = lib.KVS_GetVelParamsBlock
KVS_GetVelParamsBlock.restype = c_short
KVS_GetVelParamsBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_GetVelParamsBlock(serial_number)

    return output


KVS_HasLastMsgTimerOverrun = lib.KVS_HasLastMsgTimerOverrun
KVS_HasLastMsgTimerOverrun.restype = c_bool
KVS_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by KVS_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_HasLastMsgTimerOverrun(serial_number)

    return output


KVS_Home = lib.KVS_Home
KVS_Home.restype = c_short
KVS_Home.argtypes = [POINTER(c_char)]


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

    output = KVS_Home(serial_number)

    return output


KVS_Identify = lib.KVS_Identify
KVS_Identify.restype = c_void_p
KVS_Identify.argtypes = [POINTER(c_char)]


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

    output = KVS_Identify(serial_number)

    return output


KVS_LoadNamedSettings = lib.KVS_LoadNamedSettings
KVS_LoadNamedSettings.restype = c_bool
KVS_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    output = KVS_LoadNamedSettings(serial_number)

    return output


KVS_LoadSettings = lib.KVS_LoadSettings
KVS_LoadSettings.restype = c_bool
KVS_LoadSettings.argtypes = [POINTER(c_char)]


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

    output = KVS_LoadSettings(serial_number)

    return output


KVS_MessageQueueSize = lib.KVS_MessageQueueSize
KVS_MessageQueueSize.restype = c_int
KVS_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    output = KVS_MessageQueueSize(serial_number)

    return output


KVS_MoveAbsolute = lib.KVS_MoveAbsolute
KVS_MoveAbsolute.restype = c_short
KVS_MoveAbsolute.argtypes = [POINTER(c_char)]


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

    output = KVS_MoveAbsolute(serial_number)

    return output


KVS_MoveAtVelocity = lib.KVS_MoveAtVelocity
KVS_MoveAtVelocity.restype = c_short
KVS_MoveAtVelocity.argtypes = [POINTER(c_char)]


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

    output = KVS_MoveAtVelocity(serial_number)

    return output


KVS_MoveJog = lib.KVS_MoveJog
KVS_MoveJog.restype = c_short
KVS_MoveJog.argtypes = [POINTER(c_char)]


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

    output = KVS_MoveJog(serial_number)

    return output


KVS_MoveRelative = lib.KVS_MoveRelative
KVS_MoveRelative.restype = c_short
KVS_MoveRelative.argtypes = [POINTER(c_char)]


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

    output = KVS_MoveRelative(serial_number)

    return output


KVS_MoveRelativeDistance = lib.KVS_MoveRelativeDistance
KVS_MoveRelativeDistance.restype = c_short
KVS_MoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    output = KVS_MoveRelativeDistance(serial_number)

    return output


KVS_MoveToPosition = lib.KVS_MoveToPosition
KVS_MoveToPosition.restype = c_short
KVS_MoveToPosition.argtypes = [POINTER(c_char)]


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

    output = KVS_MoveToPosition(serial_number)

    return output


KVS_NeedsHoming = lib.KVS_NeedsHoming
KVS_NeedsHoming.restype = c_bool
KVS_NeedsHoming.argtypes = [POINTER(c_char)]


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

    output = KVS_NeedsHoming(serial_number)

    return output


KVS_Open = lib.KVS_Open
KVS_Open.restype = c_short
KVS_Open.argtypes = [POINTER(c_char)]


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

    output = KVS_Open(serial_number)

    return output


KVS_PersistSettings = lib.KVS_PersistSettings
KVS_PersistSettings.restype = c_bool
KVS_PersistSettings.argtypes = [POINTER(c_char)]


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

    output = KVS_PersistSettings(serial_number)

    return output


KVS_PollingDuration = lib.KVS_PollingDuration
KVS_PollingDuration.restype = c_long
KVS_PollingDuration.argtypes = [POINTER(c_char)]


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

    output = KVS_PollingDuration(serial_number)

    return output


KVS_RegisterMessageCallback = lib.KVS_RegisterMessageCallback
KVS_RegisterMessageCallback.restype = c_void_p
KVS_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    output = KVS_RegisterMessageCallback(serial_number)

    return output


KVS_RequestBacklash = lib.KVS_RequestBacklash
KVS_RequestBacklash.restype = c_short
KVS_RequestBacklash.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestBacklash(serial_number)

    return output


KVS_RequestDCPIDParams = lib.KVS_RequestDCPIDParams
KVS_RequestDCPIDParams.restype = c_short
KVS_RequestDCPIDParams.argtypes = [POINTER(c_char)]


def request_d_c_p_i_d_params(serial_number):
    '''
    Request the PID parameters for DC motors used in an algorithm involving calculus.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestDCPIDParams(serial_number)

    return output


KVS_RequestDigitalOutputs = lib.KVS_RequestDigitalOutputs
KVS_RequestDigitalOutputs.restype = c_short
KVS_RequestDigitalOutputs.argtypes = [POINTER(c_char)]


def request_digital_outputs(serial_number):
    '''
    Requests the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestDigitalOutputs(serial_number)

    return output


KVS_RequestEncoderCounter = lib.KVS_RequestEncoderCounter
KVS_RequestEncoderCounter.restype = c_short
KVS_RequestEncoderCounter.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestEncoderCounter(serial_number)

    return output


KVS_RequestEncoderResolutionParams = lib.KVS_RequestEncoderResolutionParams
KVS_RequestEncoderResolutionParams.restype = c_short
KVS_RequestEncoderResolutionParams.argtypes = [POINTER(c_char)]


def request_encoder_resolution_params(serial_number):
    '''
    Requests the encoder resolution parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestEncoderResolutionParams(serial_number)

    return output


KVS_RequestFrontPanelLocked = lib.KVS_RequestFrontPanelLocked
KVS_RequestFrontPanelLocked.restype = c_short
KVS_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    '''
    Ask the device if its front panel is locked.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestFrontPanelLocked(serial_number)

    return output


KVS_RequestHomingParams = lib.KVS_RequestHomingParams
KVS_RequestHomingParams.restype = c_short
KVS_RequestHomingParams.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestHomingParams(serial_number)

    return output


KVS_RequestJogParams = lib.KVS_RequestJogParams
KVS_RequestJogParams.restype = c_short
KVS_RequestJogParams.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestJogParams(serial_number)

    return output


KVS_RequestLEDswitches = lib.KVS_RequestLEDswitches
KVS_RequestLEDswitches.restype = c_short
KVS_RequestLEDswitches.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestLEDswitches(serial_number)

    return output


KVS_RequestMoveAbsolutePosition = lib.KVS_RequestMoveAbsolutePosition
KVS_RequestMoveAbsolutePosition.restype = c_short
KVS_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestMoveAbsolutePosition(serial_number)

    return output


KVS_RequestMoveRelativeDistance = lib.KVS_RequestMoveRelativeDistance
KVS_RequestMoveRelativeDistance.restype = c_short
KVS_RequestMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestMoveRelativeDistance(serial_number)

    return output


KVS_RequestPosTriggerParams = lib.KVS_RequestPosTriggerParams
KVS_RequestPosTriggerParams.restype = c_short
KVS_RequestPosTriggerParams.argtypes = [POINTER(c_char)]


def request_pos_trigger_params(serial_number):
    '''
    Requests the position trigger parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestPosTriggerParams(serial_number)

    return output


KVS_RequestPosition = lib.KVS_RequestPosition
KVS_RequestPosition.restype = c_short
KVS_RequestPosition.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestPosition(serial_number)

    return output


KVS_RequestSettings = lib.KVS_RequestSettings
KVS_RequestSettings.restype = c_short
KVS_RequestSettings.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestSettings(serial_number)

    return output


KVS_RequestStatusBits = lib.KVS_RequestStatusBits
KVS_RequestStatusBits.restype = c_short
KVS_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    output = KVS_RequestStatusBits(serial_number)

    return output


KVS_RequestTrackSettleParams = lib.KVS_RequestTrackSettleParams
KVS_RequestTrackSettleParams.restype = c_short
KVS_RequestTrackSettleParams.argtypes = [POINTER(c_char)]


def request_track_settle_params(serial_number):
    '''
    Requests the track settled parameters used to decide when settled at right position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestTrackSettleParams(serial_number)

    return output


KVS_RequestTriggerConfigParams = lib.KVS_RequestTriggerConfigParams
KVS_RequestTriggerConfigParams.restype = c_short
KVS_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    '''
    Requests the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestTriggerConfigParams(serial_number)

    return output


KVS_RequestVelParams = lib.KVS_RequestVelParams
KVS_RequestVelParams.restype = c_short
KVS_RequestVelParams.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_RequestVelParams(serial_number)

    return output


KVS_ResetStageToDefaults = lib.KVS_ResetStageToDefaults
KVS_ResetStageToDefaults.restype = c_short
KVS_ResetStageToDefaults.argtypes = [POINTER(c_char)]


def reset_stage_to_defaults(serial_number):
    '''
    Reset the stage settings to defaults.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KVS_ResetStageToDefaults(serial_number)

    return output


KVS_ResumeMoveMessages = lib.KVS_ResumeMoveMessages
KVS_ResumeMoveMessages.restype = c_short
KVS_ResumeMoveMessages.argtypes = [POINTER(c_char)]


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

    output = KVS_ResumeMoveMessages(serial_number)

    return output


KVS_SetBacklash = lib.KVS_SetBacklash
KVS_SetBacklash.restype = c_short
KVS_SetBacklash.argtypes = [POINTER(c_char)]


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

    output = KVS_SetBacklash(serial_number)

    return output


KVS_SetDCPIDParams = lib.KVS_SetDCPIDParams
KVS_SetDCPIDParams.restype = c_short
KVS_SetDCPIDParams.argtypes = [POINTER(c_char)]


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

    output = KVS_SetDCPIDParams(serial_number)

    return output


KVS_SetDigitalOutputs = lib.KVS_SetDigitalOutputs
KVS_SetDigitalOutputs.restype = c_short
KVS_SetDigitalOutputs.argtypes = [POINTER(c_char)]


def set_digital_outputs(serial_number):
    '''
    Sets the digital output bits.

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

    output = KVS_SetDigitalOutputs(serial_number)

    return output


KVS_SetDirection = lib.KVS_SetDirection
KVS_SetDirection.restype = c_void_p
KVS_SetDirection.argtypes = [POINTER(c_char)]


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

    output = KVS_SetDirection(serial_number)

    return output


KVS_SetEncoderCounter = lib.KVS_SetEncoderCounter
KVS_SetEncoderCounter.restype = c_short
KVS_SetEncoderCounter.argtypes = [POINTER(c_char)]


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

    output = KVS_SetEncoderCounter(serial_number)

    return output


KVS_SetFrontPanelLock = lib.KVS_SetFrontPanelLock
KVS_SetFrontPanelLock.restype = c_short
KVS_SetFrontPanelLock.argtypes = [POINTER(c_char)]


def set_front_panel_lock(serial_number):
    '''
    Sets the device front panel lock state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        locked: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    locked = c_bool()

    output = KVS_SetFrontPanelLock(serial_number)

    return output


KVS_SetHomingParamsBlock = lib.KVS_SetHomingParamsBlock
KVS_SetHomingParamsBlock.restype = c_short
KVS_SetHomingParamsBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_SetHomingParamsBlock(serial_number)

    return output


KVS_SetHomingVelocity = lib.KVS_SetHomingVelocity
KVS_SetHomingVelocity.restype = c_short
KVS_SetHomingVelocity.argtypes = [POINTER(c_char)]


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

    output = KVS_SetHomingVelocity(serial_number)

    return output


KVS_SetJogMode = lib.KVS_SetJogMode
KVS_SetJogMode.restype = c_short
KVS_SetJogMode.argtypes = [POINTER(c_char)]


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

    output = KVS_SetJogMode(serial_number)

    return output


KVS_SetJogParamsBlock = lib.KVS_SetJogParamsBlock
KVS_SetJogParamsBlock.restype = c_short
KVS_SetJogParamsBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_SetJogParamsBlock(serial_number)

    return output


KVS_SetJogStepSize = lib.KVS_SetJogStepSize
KVS_SetJogStepSize.restype = c_short
KVS_SetJogStepSize.argtypes = [POINTER(c_char)]


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

    output = KVS_SetJogStepSize(serial_number)

    return output


KVS_SetJogVelParams = lib.KVS_SetJogVelParams
KVS_SetJogVelParams.restype = c_short
KVS_SetJogVelParams.argtypes = [POINTER(c_char)]


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

    output = KVS_SetJogVelParams(serial_number)

    return output


KVS_SetLEDswitches = lib.KVS_SetLEDswitches
KVS_SetLEDswitches.restype = c_short
KVS_SetLEDswitches.argtypes = [POINTER(c_char)]


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

    output = KVS_SetLEDswitches(serial_number)

    return output


KVS_SetLimitsSoftwareApproachPolicy = lib.KVS_SetLimitsSoftwareApproachPolicy
KVS_SetLimitsSoftwareApproachPolicy.restype = c_void_p
KVS_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char)]


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

    output = KVS_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


KVS_SetMotorParams = lib.KVS_SetMotorParams
KVS_SetMotorParams.restype = c_short
KVS_SetMotorParams.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMotorParams(serial_number)

    return output


KVS_SetMotorParamsExt = lib.KVS_SetMotorParamsExt
KVS_SetMotorParamsExt.restype = c_short
KVS_SetMotorParamsExt.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMotorParamsExt(serial_number)

    return output


KVS_SetMotorTravelLimits = lib.KVS_SetMotorTravelLimits
KVS_SetMotorTravelLimits.restype = c_short
KVS_SetMotorTravelLimits.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMotorTravelLimits(serial_number)

    return output


KVS_SetMotorTravelMode = lib.KVS_SetMotorTravelMode
KVS_SetMotorTravelMode.restype = c_short
KVS_SetMotorTravelMode.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMotorTravelMode(serial_number)

    return output


KVS_SetMotorVelocityLimits = lib.KVS_SetMotorVelocityLimits
KVS_SetMotorVelocityLimits.restype = c_short
KVS_SetMotorVelocityLimits.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMotorVelocityLimits(serial_number)

    return output


KVS_SetMoveAbsolutePosition = lib.KVS_SetMoveAbsolutePosition
KVS_SetMoveAbsolutePosition.restype = c_short
KVS_SetMoveAbsolutePosition.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMoveAbsolutePosition(serial_number)

    return output


KVS_SetMoveRelativeDistance = lib.KVS_SetMoveRelativeDistance
KVS_SetMoveRelativeDistance.restype = c_short
KVS_SetMoveRelativeDistance.argtypes = [POINTER(c_char)]


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

    output = KVS_SetMoveRelativeDistance(serial_number)

    return output


KVS_SetPositionCounter = lib.KVS_SetPositionCounter
KVS_SetPositionCounter.restype = c_short
KVS_SetPositionCounter.argtypes = [POINTER(c_char)]


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

    output = KVS_SetPositionCounter(serial_number)

    return output


KVS_SetStageAxisLimits = lib.KVS_SetStageAxisLimits
KVS_SetStageAxisLimits.restype = c_short
KVS_SetStageAxisLimits.argtypes = [POINTER(c_char)]


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

    output = KVS_SetStageAxisLimits(serial_number)

    return output


KVS_SetTrackSettleParams = lib.KVS_SetTrackSettleParams
KVS_SetTrackSettleParams.restype = c_short
KVS_SetTrackSettleParams.argtypes = [POINTER(c_char)]


def set_track_settle_params(serial_number):
    '''
    Sets the track settled parameters used to decide when settled at right position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        settleParams: MOT_BrushlessTrackSettleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    settleParams = MOT_BrushlessTrackSettleParameters()

    output = KVS_SetTrackSettleParams(serial_number)

    return output


KVS_SetTriggerConfigParams = lib.KVS_SetTriggerConfigParams
KVS_SetTriggerConfigParams.restype = c_short
KVS_SetTriggerConfigParams.argtypes = [POINTER(c_char)]


def set_trigger_config_params(serial_number):
    '''
    Set the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KMOT_TriggerPortMode
        trigger1Polarity: KMOT_TriggerPortPolarity
        trigger2Mode: KMOT_TriggerPortMode
        trigger2Polarity: KMOT_TriggerPortPolarity

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = KVS_SetTriggerConfigParams(serial_number)

    return output


KVS_SetTriggerConfigParamsBlock = lib.KVS_SetTriggerConfigParamsBlock
KVS_SetTriggerConfigParamsBlock.restype = c_short
KVS_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char)]


def set_trigger_config_params_block(serial_number):
    '''
    Sets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KMOT_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerConfigParams = KMOT_TriggerConfig()

    output = KVS_SetTriggerConfigParamsBlock(serial_number)

    return output


KVS_SetTriggerParamsParams = lib.KVS_SetTriggerParamsParams
KVS_SetTriggerParamsParams.restype = c_short
KVS_SetTriggerParamsParams.argtypes = [POINTER(c_char)]


def set_trigger_params_params(serial_number):
    '''
    Set the Trigger Parameters Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerStartPositionFwd: c_int32
        triggerIntervalFwd: c_int32
        triggerPulseCountFwd: c_int32
        triggerStartPositionRev: c_int32
        triggerIntervalRev: c_int32
        triggerPulseCountRev: c_int32
        triggerPulseWidth: c_int32
        cycleCount: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = KVS_SetTriggerParamsParams(serial_number)

    return output


KVS_SetTriggerParamsParamsBlock = lib.KVS_SetTriggerParamsParamsBlock
KVS_SetTriggerParamsParamsBlock.restype = c_short
KVS_SetTriggerParamsParamsBlock.argtypes = [POINTER(c_char)]


def set_trigger_params_params_block(serial_number):
    '''
    Sets the trigger parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerParamsParams: KMOT_TriggerParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerParamsParams = KMOT_TriggerParams()

    output = KVS_SetTriggerParamsParamsBlock(serial_number)

    return output


KVS_SetVelParams = lib.KVS_SetVelParams
KVS_SetVelParams.restype = c_short
KVS_SetVelParams.argtypes = [POINTER(c_char)]


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

    output = KVS_SetVelParams(serial_number)

    return output


KVS_SetVelParamsBlock = lib.KVS_SetVelParamsBlock
KVS_SetVelParamsBlock.restype = c_short
KVS_SetVelParamsBlock.argtypes = [POINTER(c_char)]


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

    output = KVS_SetVelParamsBlock(serial_number)

    return output


KVS_StartPolling = lib.KVS_StartPolling
KVS_StartPolling.restype = c_bool
KVS_StartPolling.argtypes = [POINTER(c_char)]


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

    output = KVS_StartPolling(serial_number)

    return output


KVS_StopImmediate = lib.KVS_StopImmediate
KVS_StopImmediate.restype = c_short
KVS_StopImmediate.argtypes = [POINTER(c_char)]


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

    output = KVS_StopImmediate(serial_number)

    return output


KVS_StopPolling = lib.KVS_StopPolling
KVS_StopPolling.restype = c_void_p
KVS_StopPolling.argtypes = [POINTER(c_char)]


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

    output = KVS_StopPolling(serial_number)

    return output


KVS_StopProfiled = lib.KVS_StopProfiled
KVS_StopProfiled.restype = c_short
KVS_StopProfiled.argtypes = [POINTER(c_char)]


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

    output = KVS_StopProfiled(serial_number)

    return output


KVS_SuspendMoveMessages = lib.KVS_SuspendMoveMessages
KVS_SuspendMoveMessages.restype = c_short
KVS_SuspendMoveMessages.argtypes = [POINTER(c_char)]


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

    output = KVS_SuspendMoveMessages(serial_number)

    return output


KVS_TimeSinceLastMsgReceived = lib.KVS_TimeSinceLastMsgReceived
KVS_TimeSinceLastMsgReceived.restype = c_bool
KVS_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


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

    output = KVS_TimeSinceLastMsgReceived(serial_number)

    return output


KVS_WaitForMessage = lib.KVS_WaitForMessage
KVS_WaitForMessage.restype = c_bool
KVS_WaitForMessage.argtypes = [POINTER(c_char)]


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

    output = KVS_WaitForMessage(serial_number)

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


