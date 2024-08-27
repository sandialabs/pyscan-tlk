from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_int,
    c_int16,
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
    KMOT_TriggerPortMode,
    KMOT_TriggerPortPolarity,
    KMOT_WheelDirectionSense,
    KMOT_WheelMode,
    MOT_JogModes,
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
    MOT_BrushlessCurrentLoopParameters,
    MOT_BrushlessElectricOutputParameters,
    MOT_BrushlessPositionLoopParameters,
    MOT_BrushlessTrackSettleParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_StageAxisParameters,
    MOT_VelocityParameters,
    MOT_VelocityProfileParameters,
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
    lib_path + "Thorlabs.MotionControl.KCube.BrushlessMotor.dll")

BMC_CanDeviceLockFrontPanel = lib.BMC_CanDeviceLockFrontPanel
BMC_CanDeviceLockFrontPanel.restype = c_bool
BMC_CanDeviceLockFrontPanel.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = BMC_CanDeviceLockFrontPanel(serial_number)

    return output


BMC_CanHome = lib.BMC_CanHome
BMC_CanHome.restype = c_bool
BMC_CanHome.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_CanHome(serial_number)

    return output


BMC_CanMoveWithoutHomingFirst = lib.BMC_CanMoveWithoutHomingFirst
BMC_CanMoveWithoutHomingFirst.restype = c_bool
BMC_CanMoveWithoutHomingFirst.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_CanMoveWithoutHomingFirst(serial_number)

    return output


BMC_CheckConnection = lib.BMC_CheckConnection
BMC_CheckConnection.restype = c_bool
BMC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = BMC_CheckConnection(serial_number)

    return output


BMC_ClearMessageQueue = lib.BMC_ClearMessageQueue
BMC_ClearMessageQueue.restype = c_short
BMC_ClearMessageQueue.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_ClearMessageQueue(serial_number)

    return output


BMC_Close = lib.BMC_Close
BMC_Close.restype = c_short
BMC_Close.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = BMC_Close(serial_number)

    return output


BMC_DisableChannel = lib.BMC_DisableChannel
BMC_DisableChannel.restype = c_short
BMC_DisableChannel.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_DisableChannel(serial_number)

    return output


BMC_EnableChannel = lib.BMC_EnableChannel
BMC_EnableChannel.restype = c_short
BMC_EnableChannel.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_EnableChannel(serial_number)

    return output


BMC_EnableLastMsgTimer = lib.BMC_EnableLastMsgTimer
BMC_EnableLastMsgTimer.restype = c_void_p
BMC_EnableLastMsgTimer.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = BMC_EnableLastMsgTimer(serial_number)

    return output


BMC_GetBacklash = lib.BMC_GetBacklash
BMC_GetBacklash.restype = c_long
BMC_GetBacklash.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetBacklash(serial_number)

    return output


BMC_GetCurrentLoopParams = lib.BMC_GetCurrentLoopParams
BMC_GetCurrentLoopParams.restype = c_short
BMC_GetCurrentLoopParams.argtypes = []


def get_current_loop_params(serial_number):
    '''
    Gets the current loop parameters for moving to required position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        currentLoopParams: MOT_BrushlessCurrentLoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    currentLoopParams = MOT_BrushlessCurrentLoopParameters()

    output = BMC_GetCurrentLoopParams(serial_number)

    return output


BMC_GetDeviceUnitFromRealValue = lib.BMC_GetDeviceUnitFromRealValue
BMC_GetDeviceUnitFromRealValue.restype = c_short
BMC_GetDeviceUnitFromRealValue.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = BMC_GetDeviceUnitFromRealValue(serial_number)

    return output


BMC_GetDigitalOutputs = lib.BMC_GetDigitalOutputs
BMC_GetDigitalOutputs.restype = c_byte
BMC_GetDigitalOutputs.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetDigitalOutputs(serial_number)

    return output


BMC_GetElectricOutputParams = lib.BMC_GetElectricOutputParams
BMC_GetElectricOutputParams.restype = c_short
BMC_GetElectricOutputParams.argtypes = []


def get_electric_output_params(serial_number):
    '''
    Gets the electric output parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        electricOutputParams: MOT_BrushlessElectricOutputParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    electricOutputParams = MOT_BrushlessElectricOutputParameters()

    output = BMC_GetElectricOutputParams(serial_number)

    return output


BMC_GetEncoderCounter = lib.BMC_GetEncoderCounter
BMC_GetEncoderCounter.restype = c_long
BMC_GetEncoderCounter.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetEncoderCounter(serial_number)

    return output


BMC_GetFirmwareVersion = lib.BMC_GetFirmwareVersion
BMC_GetFirmwareVersion.restype = c_ulong
BMC_GetFirmwareVersion.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetFirmwareVersion(serial_number)

    return output


BMC_GetFrontPanelLocked = lib.BMC_GetFrontPanelLocked
BMC_GetFrontPanelLocked.restype = c_bool
BMC_GetFrontPanelLocked.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = BMC_GetFrontPanelLocked(serial_number)

    return output


BMC_GetHardwareInfo = lib.BMC_GetHardwareInfo
BMC_GetHardwareInfo.restype = c_short
BMC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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
    channel = c_short()
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_short()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = BMC_GetHardwareInfo(serial_number)

    return output


BMC_GetHardwareInfoBlock = lib.BMC_GetHardwareInfoBlock
BMC_GetHardwareInfoBlock.restype = c_short
BMC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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
    channel = c_short()
    hardwareInfo = TLI_HardwareInformation()

    output = BMC_GetHardwareInfoBlock(serial_number)

    return output


BMC_GetHomingParamsBlock = lib.BMC_GetHomingParamsBlock
BMC_GetHomingParamsBlock.restype = c_short
BMC_GetHomingParamsBlock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = BMC_GetHomingParamsBlock(serial_number)

    return output


BMC_GetHomingVelocity = lib.BMC_GetHomingVelocity
BMC_GetHomingVelocity.restype = c_uint
BMC_GetHomingVelocity.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetHomingVelocity(serial_number)

    return output


BMC_GetJogMode = lib.BMC_GetJogMode
BMC_GetJogMode.restype = c_short
BMC_GetJogMode.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BMC_GetJogMode(serial_number)

    return output


BMC_GetJogParamsBlock = lib.BMC_GetJogParamsBlock
BMC_GetJogParamsBlock.restype = c_short
BMC_GetJogParamsBlock.argtypes = []


def get_jog_params_block(serial_number):
    '''
    Get the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        jogParams: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    jogParams = MOT_JogParameters()

    output = BMC_GetJogParamsBlock(serial_number)

    return output


BMC_GetJogStepSize = lib.BMC_GetJogStepSize
BMC_GetJogStepSize.restype = c_uint
BMC_GetJogStepSize.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetJogStepSize(serial_number)

    return output


BMC_GetJogVelParams = lib.BMC_GetJogVelParams
BMC_GetJogVelParams.restype = c_short
BMC_GetJogVelParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_GetJogVelParams(serial_number)

    return output


BMC_GetMMIParams = lib.BMC_GetMMIParams
BMC_GetMMIParams.restype = c_short
BMC_GetMMIParams.argtypes = []


def get_m_m_i_params(serial_number):
    '''
    Get the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KMOT_WheelMode
        wheelMaxVelocity: c_int32
        wheelAcceleration: c_int32
        directionSense: KMOT_WheelDirectionSense
        presetPosition1: c_int32
        presetPosition2: c_int32
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = BMC_GetMMIParams(serial_number)

    return output


BMC_GetMMIParamsBlock = lib.BMC_GetMMIParamsBlock
BMC_GetMMIParamsBlock.restype = c_short
BMC_GetMMIParamsBlock.argtypes = []


def get_m_m_i_params_block(serial_number):
    '''
    Gets the MMI parameters for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mmiParams: KMOT_MMIParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mmiParams = KMOT_MMIParams()

    output = BMC_GetMMIParamsBlock(serial_number)

    return output


BMC_GetMMIParamsExt = lib.BMC_GetMMIParamsExt
BMC_GetMMIParamsExt.restype = c_short
BMC_GetMMIParamsExt.argtypes = []


def get_m_m_i_params_ext(serial_number):
    '''
    Get the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KMOT_WheelMode
        wheelMaxVelocity: c_int32
        wheelAcceleration: c_int32
        directionSense: KMOT_WheelDirectionSense
        presetPosition1: c_int32
        presetPosition2: c_int32
        displayIntensity: c_int16
        displayTimeout: c_int16
        displayDimIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = BMC_GetMMIParamsExt(serial_number)

    return output


BMC_GetMotorParams = lib.BMC_GetMotorParams
BMC_GetMotorParams.restype = c_short
BMC_GetMotorParams.argtypes = []


def get_motor_params(serial_number):
    '''
    Get the motor parameters for the Brushless Votor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        countsPerUnit: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    countsPerUnit = c_long()

    output = BMC_GetMotorParams(serial_number)

    return output


BMC_GetMotorParamsExt = lib.BMC_GetMotorParamsExt
BMC_GetMotorParamsExt.restype = c_short
BMC_GetMotorParamsExt.argtypes = []


def get_motor_params_ext(serial_number):
    '''
    Get the motor parameters for the Brushless Votor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        countsPerUnit: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    countsPerUnit = c_double()

    output = BMC_GetMotorParamsExt(serial_number)

    return output


BMC_GetMotorTravelLimits = lib.BMC_GetMotorTravelLimits
BMC_GetMotorTravelLimits.restype = c_short
BMC_GetMotorTravelLimits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = BMC_GetMotorTravelLimits(serial_number)

    return output


BMC_GetMotorTravelMode = lib.BMC_GetMotorTravelMode
BMC_GetMotorTravelMode.restype = MOT_TravelModes
BMC_GetMotorTravelMode.argtypes = []


def get_motor_travel_mode(serial_number):
    '''
    Get motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        MOT_TravelModes
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetMotorTravelMode(serial_number)

    return output


BMC_GetMotorVelocityLimits = lib.BMC_GetMotorVelocityLimits
BMC_GetMotorVelocityLimits.restype = c_short
BMC_GetMotorVelocityLimits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BMC_GetMotorVelocityLimits(serial_number)

    return output


BMC_GetMoveAbsolutePosition = lib.BMC_GetMoveAbsolutePosition
BMC_GetMoveAbsolutePosition.restype = c_int
BMC_GetMoveAbsolutePosition.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetMoveAbsolutePosition(serial_number)

    return output


BMC_GetMoveRelativeDistance = lib.BMC_GetMoveRelativeDistance
BMC_GetMoveRelativeDistance.restype = c_int
BMC_GetMoveRelativeDistance.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetMoveRelativeDistance(serial_number)

    return output


BMC_GetNextMessage = lib.BMC_GetNextMessage
BMC_GetNextMessage.restype = c_bool
BMC_GetNextMessage.argtypes = []


def get_next_message(serial_number):
    '''
    Get the next MessageQueue item.

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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BMC_GetNextMessage(serial_number)

    return output


BMC_GetNumberPositions = lib.BMC_GetNumberPositions
BMC_GetNumberPositions.restype = c_int
BMC_GetNumberPositions.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetNumberPositions(serial_number)

    return output


BMC_GetPosLoopParams = lib.BMC_GetPosLoopParams
BMC_GetPosLoopParams.restype = c_short
BMC_GetPosLoopParams.argtypes = []


def get_pos_loop_params(serial_number):
    '''
    Gets the position feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        positionLoopParams: MOT_BrushlessPositionLoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    positionLoopParams = MOT_BrushlessPositionLoopParameters()

    output = BMC_GetPosLoopParams(serial_number)

    return output


BMC_GetPosition = lib.BMC_GetPosition
BMC_GetPosition.restype = c_int
BMC_GetPosition.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetPosition(serial_number)

    return output


BMC_GetPositionCounter = lib.BMC_GetPositionCounter
BMC_GetPositionCounter.restype = c_long
BMC_GetPositionCounter.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetPositionCounter(serial_number)

    return output


BMC_GetRealValueFromDeviceUnit = lib.BMC_GetRealValueFromDeviceUnit
BMC_GetRealValueFromDeviceUnit.restype = c_short
BMC_GetRealValueFromDeviceUnit.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = BMC_GetRealValueFromDeviceUnit(serial_number)

    return output


BMC_GetSoftLimitMode = lib.BMC_GetSoftLimitMode
BMC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BMC_GetSoftLimitMode.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetSoftLimitMode(serial_number)

    return output


BMC_GetSoftwareVersion = lib.BMC_GetSoftwareVersion
BMC_GetSoftwareVersion.restype = c_ulong
BMC_GetSoftwareVersion.argtypes = []


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

    output = BMC_GetSoftwareVersion(serial_number)

    return output


BMC_GetStageAxisMaxPos = lib.BMC_GetStageAxisMaxPos
BMC_GetStageAxisMaxPos.restype = c_int
BMC_GetStageAxisMaxPos.argtypes = []


def get_stage_axis_max_pos(serial_number):
    '''
    Gets the Brushless Motor stage axis maximum position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetStageAxisMaxPos(serial_number)

    return output


BMC_GetStageAxisMinPos = lib.BMC_GetStageAxisMinPos
BMC_GetStageAxisMinPos.restype = c_int
BMC_GetStageAxisMinPos.argtypes = []


def get_stage_axis_min_pos(serial_number):
    '''
    Gets the Brushless Motor stage axis minimum position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetStageAxisMinPos(serial_number)

    return output


BMC_GetStageAxisParams = lib.BMC_GetStageAxisParams
BMC_GetStageAxisParams.restype = c_short
BMC_GetStageAxisParams.argtypes = []


def get_stage_axis_params(serial_number):
    '''
    Gets the Brushless Motor stage axis parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stageID: c_long
        axisID: c_long
        partNumber: POINTER(c_char)
        size: c_ulong
        serialNumber: c_ulong
        countsPerUnit: c_ulong
        minPosition: c_int
        maxPosition: c_int
        maxAcceleration: c_int
        maxDecceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stageID = c_long()
    axisID = c_long()
    partNumber = POINTER(c_char)()
    size = c_ulong()
    serialNumber = c_ulong()
    countsPerUnit = c_ulong()
    minPosition = c_int()
    maxPosition = c_int()
    maxAcceleration = c_int()
    maxDecceleration = c_int()
    maxVelocity = c_int()

    output = BMC_GetStageAxisParams(serial_number)

    return output


BMC_GetStageAxisParamsBlock = lib.BMC_GetStageAxisParamsBlock
BMC_GetStageAxisParamsBlock.restype = c_short
BMC_GetStageAxisParamsBlock.argtypes = []


def get_stage_axis_params_block(serial_number):
    '''
    Gets the Brushless Motor stage axis parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        stageAxisParams: MOT_StageAxisParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stageAxisParams = MOT_StageAxisParameters()

    output = BMC_GetStageAxisParamsBlock(serial_number)

    return output


BMC_GetStatusBits = lib.BMC_GetStatusBits
BMC_GetStatusBits.restype = c_ulong
BMC_GetStatusBits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetStatusBits(serial_number)

    return output


BMC_GetTrackSettleParams = lib.BMC_GetTrackSettleParams
BMC_GetTrackSettleParams.restype = c_short
BMC_GetTrackSettleParams.argtypes = []


def get_track_settle_params(serial_number):
    '''
    Gets the track settled parameters used to decide when settled at right position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        settleParams: MOT_BrushlessTrackSettleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    settleParams = MOT_BrushlessTrackSettleParameters()

    output = BMC_GetTrackSettleParams(serial_number)

    return output


BMC_GetTriggerConfigParams = lib.BMC_GetTriggerConfigParams
BMC_GetTriggerConfigParams.restype = c_short
BMC_GetTriggerConfigParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BMC_GetTriggerConfigParams(serial_number)

    return output


BMC_GetTriggerConfigParamsBlock = lib.BMC_GetTriggerConfigParamsBlock
BMC_GetTriggerConfigParamsBlock.restype = c_short
BMC_GetTriggerConfigParamsBlock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    triggerConfigParams = KMOT_TriggerConfig()

    output = BMC_GetTriggerConfigParamsBlock(serial_number)

    return output


BMC_GetTriggerParamsParams = lib.BMC_GetTriggerParamsParams
BMC_GetTriggerParamsParams.restype = c_short
BMC_GetTriggerParamsParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BMC_GetTriggerParamsParams(serial_number)

    return output


BMC_GetTriggerParamsParamsBlock = lib.BMC_GetTriggerParamsParamsBlock
BMC_GetTriggerParamsParamsBlock.restype = c_short
BMC_GetTriggerParamsParamsBlock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    triggerParamsParams = KMOT_TriggerParams()

    output = BMC_GetTriggerParamsParamsBlock(serial_number)

    return output


BMC_GetTriggerSwitches = lib.BMC_GetTriggerSwitches
BMC_GetTriggerSwitches.restype = c_byte
BMC_GetTriggerSwitches.argtypes = []


def get_trigger_switches(serial_number):
    '''
    Gets the trigger switch bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_GetTriggerSwitches(serial_number)

    return output


BMC_GetVelParams = lib.BMC_GetVelParams
BMC_GetVelParams.restype = c_short
BMC_GetVelParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_GetVelParams(serial_number)

    return output


BMC_GetVelParamsBlock = lib.BMC_GetVelParamsBlock
BMC_GetVelParamsBlock.restype = c_short
BMC_GetVelParamsBlock.argtypes = []


def get_vel_params_block(serial_number):
    '''
    Get the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocityParams: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()

    output = BMC_GetVelParamsBlock(serial_number)

    return output


BMC_GetVelocityProfileParams = lib.BMC_GetVelocityProfileParams
BMC_GetVelocityProfileParams.restype = c_short
BMC_GetVelocityProfileParams.argtypes = []


def get_velocity_profile_params(serial_number):
    '''
    Gets the velocity profile parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocityProfileParams: MOT_VelocityProfileParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocityProfileParams = MOT_VelocityProfileParameters()

    output = BMC_GetVelocityProfileParams(serial_number)

    return output


BMC_HasLastMsgTimerOverrun = lib.BMC_HasLastMsgTimerOverrun
BMC_HasLastMsgTimerOverrun.restype = c_bool
BMC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by BMC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_HasLastMsgTimerOverrun(serial_number)

    return output


BMC_Home = lib.BMC_Home
BMC_Home.restype = c_short
BMC_Home.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_Home(serial_number)

    return output


BMC_Identify = lib.BMC_Identify
BMC_Identify.restype = c_void_p
BMC_Identify.argtypes = []


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

    output = BMC_Identify(serial_number)

    return output


BMC_LoadNamedSettings = lib.BMC_LoadNamedSettings
BMC_LoadNamedSettings.restype = c_bool
BMC_LoadNamedSettings.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    settingsName = POINTER(c_char)()

    output = BMC_LoadNamedSettings(serial_number)

    return output


BMC_LoadSettings = lib.BMC_LoadSettings
BMC_LoadSettings.restype = c_bool
BMC_LoadSettings.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_LoadSettings(serial_number)

    return output


BMC_MessageQueueSize = lib.BMC_MessageQueueSize
BMC_MessageQueueSize.restype = c_int
BMC_MessageQueueSize.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_MessageQueueSize(serial_number)

    return output


BMC_MoveAbsolute = lib.BMC_MoveAbsolute
BMC_MoveAbsolute.restype = c_short
BMC_MoveAbsolute.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_MoveAbsolute(serial_number)

    return output


BMC_MoveAtVelocity = lib.BMC_MoveAtVelocity
BMC_MoveAtVelocity.restype = c_short
BMC_MoveAtVelocity.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    direction = MOT_TravelDirection()

    output = BMC_MoveAtVelocity(serial_number)

    return output


BMC_MoveJog = lib.BMC_MoveJog
BMC_MoveJog.restype = c_short
BMC_MoveJog.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    jogDirection = MOT_TravelDirection()

    output = BMC_MoveJog(serial_number)

    return output


BMC_MoveRelative = lib.BMC_MoveRelative
BMC_MoveRelative.restype = c_short
BMC_MoveRelative.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    displacement = c_int()

    output = BMC_MoveRelative(serial_number)

    return output


BMC_MoveRelativeDistance = lib.BMC_MoveRelativeDistance
BMC_MoveRelativeDistance.restype = c_short
BMC_MoveRelativeDistance.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_MoveRelativeDistance(serial_number)

    return output


BMC_MoveToPosition = lib.BMC_MoveToPosition
BMC_MoveToPosition.restype = c_short
BMC_MoveToPosition.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    index = c_int()

    output = BMC_MoveToPosition(serial_number)

    return output


BMC_NeedsHoming = lib.BMC_NeedsHoming
BMC_NeedsHoming.restype = c_bool
BMC_NeedsHoming.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_NeedsHoming(serial_number)

    return output


BMC_Open = lib.BMC_Open
BMC_Open.restype = c_short
BMC_Open.argtypes = []


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

    output = BMC_Open(serial_number)

    return output


BMC_OverrideHomeRequirement = lib.BMC_OverrideHomeRequirement
BMC_OverrideHomeRequirement.restype = c_short
BMC_OverrideHomeRequirement.argtypes = []


def override_home_requirement(serial_number):
    '''
    Set to allow a device to be positioned without prior homing.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_OverrideHomeRequirement(serial_number)

    return output


BMC_PersistSettings = lib.BMC_PersistSettings
BMC_PersistSettings.restype = c_bool
BMC_PersistSettings.argtypes = []


def persist_settings(serial_number):
    '''
    persist the devices current settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_PersistSettings(serial_number)

    return output


BMC_PollingDuration = lib.BMC_PollingDuration
BMC_PollingDuration.restype = c_long
BMC_PollingDuration.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_PollingDuration(serial_number)

    return output


BMC_RegisterMessageCallback = lib.BMC_RegisterMessageCallback
BMC_RegisterMessageCallback.restype = c_short
BMC_RegisterMessageCallback.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RegisterMessageCallback(serial_number)

    return output


BMC_RequestBacklash = lib.BMC_RequestBacklash
BMC_RequestBacklash.restype = c_short
BMC_RequestBacklash.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestBacklash(serial_number)

    return output


BMC_RequestCurrentLoopParams = lib.BMC_RequestCurrentLoopParams
BMC_RequestCurrentLoopParams.restype = c_short
BMC_RequestCurrentLoopParams.argtypes = []


def request_current_loop_params(serial_number):
    '''
    Requests the current loop parameters for moving to required position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestCurrentLoopParams(serial_number)

    return output


BMC_RequestDigitalOutputs = lib.BMC_RequestDigitalOutputs
BMC_RequestDigitalOutputs.restype = c_short
BMC_RequestDigitalOutputs.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestDigitalOutputs(serial_number)

    return output


BMC_RequestElectricOutputParams = lib.BMC_RequestElectricOutputParams
BMC_RequestElectricOutputParams.restype = c_short
BMC_RequestElectricOutputParams.argtypes = []


def request_electric_output_params(serial_number):
    '''
    Requests the electric output parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestElectricOutputParams(serial_number)

    return output


BMC_RequestEncoderCounter = lib.BMC_RequestEncoderCounter
BMC_RequestEncoderCounter.restype = c_short
BMC_RequestEncoderCounter.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestEncoderCounter(serial_number)

    return output


BMC_RequestFrontPanelLocked = lib.BMC_RequestFrontPanelLocked
BMC_RequestFrontPanelLocked.restype = c_short
BMC_RequestFrontPanelLocked.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = BMC_RequestFrontPanelLocked(serial_number)

    return output


BMC_RequestHomingParams = lib.BMC_RequestHomingParams
BMC_RequestHomingParams.restype = c_short
BMC_RequestHomingParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestHomingParams(serial_number)

    return output


BMC_RequestJogParams = lib.BMC_RequestJogParams
BMC_RequestJogParams.restype = c_short
BMC_RequestJogParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestJogParams(serial_number)

    return output


BMC_RequestMMIparams = lib.BMC_RequestMMIparams
BMC_RequestMMIparams.restype = c_short
BMC_RequestMMIparams.argtypes = []


def request_m_m_iparams(serial_number):
    '''
    Requests the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = BMC_RequestMMIparams(serial_number)

    return output


BMC_RequestMoveAbsolutePosition = lib.BMC_RequestMoveAbsolutePosition
BMC_RequestMoveAbsolutePosition.restype = c_short
BMC_RequestMoveAbsolutePosition.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestMoveAbsolutePosition(serial_number)

    return output


BMC_RequestMoveRelativeDistance = lib.BMC_RequestMoveRelativeDistance
BMC_RequestMoveRelativeDistance.restype = c_short
BMC_RequestMoveRelativeDistance.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestMoveRelativeDistance(serial_number)

    return output


BMC_RequestPosLoopParams = lib.BMC_RequestPosLoopParams
BMC_RequestPosLoopParams.restype = c_short
BMC_RequestPosLoopParams.argtypes = []


def request_pos_loop_params(serial_number):
    '''
    Requests the position feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestPosLoopParams(serial_number)

    return output


BMC_RequestPosTriggerParams = lib.BMC_RequestPosTriggerParams
BMC_RequestPosTriggerParams.restype = c_short
BMC_RequestPosTriggerParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = BMC_RequestPosTriggerParams(serial_number)

    return output


BMC_RequestPosition = lib.BMC_RequestPosition
BMC_RequestPosition.restype = c_short
BMC_RequestPosition.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestPosition(serial_number)

    return output


BMC_RequestSettings = lib.BMC_RequestSettings
BMC_RequestSettings.restype = c_short
BMC_RequestSettings.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestSettings(serial_number)

    return output


BMC_RequestStageAxisParams = lib.BMC_RequestStageAxisParams
BMC_RequestStageAxisParams.restype = c_short
BMC_RequestStageAxisParams.argtypes = []


def request_stage_axis_params(serial_number):
    '''
    Requests the stage axis parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestStageAxisParams(serial_number)

    return output


BMC_RequestStatusBits = lib.BMC_RequestStatusBits
BMC_RequestStatusBits.restype = c_short
BMC_RequestStatusBits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestStatusBits(serial_number)

    return output


BMC_RequestTrackSettleParams = lib.BMC_RequestTrackSettleParams
BMC_RequestTrackSettleParams.restype = c_short
BMC_RequestTrackSettleParams.argtypes = []


def request_track_settle_params(serial_number):
    '''
    Requests the parameters used to decide when settled at right position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestTrackSettleParams(serial_number)

    return output


BMC_RequestTriggerConfigParams = lib.BMC_RequestTriggerConfigParams
BMC_RequestTriggerConfigParams.restype = c_short
BMC_RequestTriggerConfigParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = BMC_RequestTriggerConfigParams(serial_number)

    return output


BMC_RequestTriggerSwitches = lib.BMC_RequestTriggerSwitches
BMC_RequestTriggerSwitches.restype = c_short
BMC_RequestTriggerSwitches.argtypes = []


def request_trigger_switches(serial_number):
    '''
    Requests the trigger switch bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestTriggerSwitches(serial_number)

    return output


BMC_RequestVelParams = lib.BMC_RequestVelParams
BMC_RequestVelParams.restype = c_short
BMC_RequestVelParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestVelParams(serial_number)

    return output


BMC_RequestVelocityProfileParams = lib.BMC_RequestVelocityProfileParams
BMC_RequestVelocityProfileParams.restype = c_short
BMC_RequestVelocityProfileParams.argtypes = []


def request_velocity_profile_params(serial_number):
    '''
    Requests the velocity profile parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_RequestVelocityProfileParams(serial_number)

    return output


BMC_ResetRotationModes = lib.BMC_ResetRotationModes
BMC_ResetRotationModes.restype = c_short
BMC_ResetRotationModes.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_ResetRotationModes(serial_number)

    return output


BMC_ResetStageToDefaults = lib.BMC_ResetStageToDefaults
BMC_ResetStageToDefaults.restype = c_short
BMC_ResetStageToDefaults.argtypes = []


def reset_stage_to_defaults(serial_number):
    '''
    Reset the stage settings to defaults.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_ResetStageToDefaults(serial_number)

    return output


BMC_ResumeMoveMessages = lib.BMC_ResumeMoveMessages
BMC_ResumeMoveMessages.restype = c_short
BMC_ResumeMoveMessages.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_ResumeMoveMessages(serial_number)

    return output


BMC_SetBacklash = lib.BMC_SetBacklash
BMC_SetBacklash.restype = c_short
BMC_SetBacklash.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    distance = c_long()

    output = BMC_SetBacklash(serial_number)

    return output


BMC_SetCurrentLoopParams = lib.BMC_SetCurrentLoopParams
BMC_SetCurrentLoopParams.restype = c_short
BMC_SetCurrentLoopParams.argtypes = []


def set_current_loop_params(serial_number):
    '''
    Sets the current loop parameters for moving to required position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        currentLoopParams: MOT_BrushlessCurrentLoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    currentLoopParams = MOT_BrushlessCurrentLoopParameters()

    output = BMC_SetCurrentLoopParams(serial_number)

    return output


BMC_SetDigitalOutputs = lib.BMC_SetDigitalOutputs
BMC_SetDigitalOutputs.restype = c_short
BMC_SetDigitalOutputs.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    outputsBits = c_byte()

    output = BMC_SetDigitalOutputs(serial_number)

    return output


BMC_SetDirection = lib.BMC_SetDirection
BMC_SetDirection.restype = c_short
BMC_SetDirection.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    reverse = c_bool()

    output = BMC_SetDirection(serial_number)

    return output


BMC_SetElectricOutputParams = lib.BMC_SetElectricOutputParams
BMC_SetElectricOutputParams.restype = c_short
BMC_SetElectricOutputParams.argtypes = []


def set_electric_output_params(serial_number):
    '''
    Sets the electric output parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        electricOutputParams: MOT_BrushlessElectricOutputParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    electricOutputParams = MOT_BrushlessElectricOutputParameters()

    output = BMC_SetElectricOutputParams(serial_number)

    return output


BMC_SetEncoderCounter = lib.BMC_SetEncoderCounter
BMC_SetEncoderCounter.restype = c_short
BMC_SetEncoderCounter.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    count = c_long()

    output = BMC_SetEncoderCounter(serial_number)

    return output


BMC_SetFrontPanelLock = lib.BMC_SetFrontPanelLock
BMC_SetFrontPanelLock.restype = c_short
BMC_SetFrontPanelLock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    locked = c_bool()

    output = BMC_SetFrontPanelLock(serial_number)

    return output


BMC_SetHomingParamsBlock = lib.BMC_SetHomingParamsBlock
BMC_SetHomingParamsBlock.restype = c_short
BMC_SetHomingParamsBlock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    homingParams = MOT_HomingParameters()

    output = BMC_SetHomingParamsBlock(serial_number)

    return output


BMC_SetHomingVelocity = lib.BMC_SetHomingVelocity
BMC_SetHomingVelocity.restype = c_short
BMC_SetHomingVelocity.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocity = c_uint()

    output = BMC_SetHomingVelocity(serial_number)

    return output


BMC_SetJogMode = lib.BMC_SetJogMode
BMC_SetJogMode.restype = c_short
BMC_SetJogMode.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = BMC_SetJogMode(serial_number)

    return output


BMC_SetJogParamsBlock = lib.BMC_SetJogParamsBlock
BMC_SetJogParamsBlock.restype = c_short
BMC_SetJogParamsBlock.argtypes = []


def set_jog_params_block(serial_number):
    '''
    Set the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        jogParams: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    jogParams = MOT_JogParameters()

    output = BMC_SetJogParamsBlock(serial_number)

    return output


BMC_SetJogStepSize = lib.BMC_SetJogStepSize
BMC_SetJogStepSize.restype = c_short
BMC_SetJogStepSize.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    stepSize = c_uint()

    output = BMC_SetJogStepSize(serial_number)

    return output


BMC_SetJogVelParams = lib.BMC_SetJogVelParams
BMC_SetJogVelParams.restype = c_short
BMC_SetJogVelParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_SetJogVelParams(serial_number)

    return output


BMC_SetLimitsSoftwareApproachPolicy = lib.BMC_SetLimitsSoftwareApproachPolicy
BMC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
BMC_SetLimitsSoftwareApproachPolicy.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = BMC_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


BMC_SetMMIParams = lib.BMC_SetMMIParams
BMC_SetMMIParams.restype = c_short
BMC_SetMMIParams.argtypes = []


def set_m_m_i_params(serial_number):
    '''
    Set the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KMOT_WheelMode
        wheelMaxVelocity: c_int32
        wheelAcceleration: c_int32
        directionSense: KMOT_WheelDirectionSense
        presetPosition1: c_int32
        presetPosition2: c_int32
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()

    output = BMC_SetMMIParams(serial_number)

    return output


BMC_SetMMIParamsBlock = lib.BMC_SetMMIParamsBlock
BMC_SetMMIParamsBlock.restype = c_short
BMC_SetMMIParamsBlock.argtypes = []


def set_m_m_i_params_block(serial_number):
    '''
    Sets the MMI parameters for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mmiParams: KMOT_MMIParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mmiParams = KMOT_MMIParams()

    output = BMC_SetMMIParamsBlock(serial_number)

    return output


BMC_SetMMIParamsExt = lib.BMC_SetMMIParamsExt
BMC_SetMMIParamsExt.restype = c_short
BMC_SetMMIParamsExt.argtypes = []


def set_m_m_i_params_ext(serial_number):
    '''
    Set the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KMOT_WheelMode
        wheelMaxVelocity: c_int32
        wheelAcceleration: c_int32
        directionSense: KMOT_WheelDirectionSense
        presetPosition1: c_int32
        presetPosition2: c_int32
        displayIntensity: c_int16
        displayTimeout: c_int16
        displayDimIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    wheelMode = KMOT_WheelMode()
    wheelMaxVelocity = c_int32()
    wheelAcceleration = c_int32()
    directionSense = KMOT_WheelDirectionSense()
    presetPosition1 = c_int32()
    presetPosition2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = BMC_SetMMIParamsExt(serial_number)

    return output


BMC_SetMotorParams = lib.BMC_SetMotorParams
BMC_SetMotorParams.restype = c_short
BMC_SetMotorParams.argtypes = []


def set_motor_params(serial_number):
    '''
    Set the motor parameters for the Brushless Votor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        countsPerUnit: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    countsPerUnit = c_long()

    output = BMC_SetMotorParams(serial_number)

    return output


BMC_SetMotorParamsExt = lib.BMC_SetMotorParamsExt
BMC_SetMotorParamsExt.restype = c_short
BMC_SetMotorParamsExt.argtypes = []


def set_motor_params_ext(serial_number):
    '''
    Set the motor parameters for the Brushless Votor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        countsPerUnit: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    countsPerUnit = c_double()

    output = BMC_SetMotorParamsExt(serial_number)

    return output


BMC_SetMotorTravelLimits = lib.BMC_SetMotorTravelLimits
BMC_SetMotorTravelLimits.restype = c_short
BMC_SetMotorTravelLimits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    minPosition = c_double()
    maxPosition = c_double()

    output = BMC_SetMotorTravelLimits(serial_number)

    return output


BMC_SetMotorTravelMode = lib.BMC_SetMotorTravelMode
BMC_SetMotorTravelMode.restype = c_short
BMC_SetMotorTravelMode.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    travelMode = MOT_TravelModes()

    output = BMC_SetMotorTravelMode(serial_number)

    return output


BMC_SetMotorVelocityLimits = lib.BMC_SetMotorVelocityLimits
BMC_SetMotorVelocityLimits.restype = c_short
BMC_SetMotorVelocityLimits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = BMC_SetMotorVelocityLimits(serial_number)

    return output


BMC_SetMoveAbsolutePosition = lib.BMC_SetMoveAbsolutePosition
BMC_SetMoveAbsolutePosition.restype = c_short
BMC_SetMoveAbsolutePosition.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    position = c_int()

    output = BMC_SetMoveAbsolutePosition(serial_number)

    return output


BMC_SetMoveRelativeDistance = lib.BMC_SetMoveRelativeDistance
BMC_SetMoveRelativeDistance.restype = c_short
BMC_SetMoveRelativeDistance.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    distance = c_int()

    output = BMC_SetMoveRelativeDistance(serial_number)

    return output


BMC_SetPosLoopParams = lib.BMC_SetPosLoopParams
BMC_SetPosLoopParams.restype = c_short
BMC_SetPosLoopParams.argtypes = []


def set_pos_loop_params(serial_number):
    '''
    Sets the position feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        positionLoopParams: MOT_BrushlessPositionLoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    positionLoopParams = MOT_BrushlessPositionLoopParameters()

    output = BMC_SetPosLoopParams(serial_number)

    return output


BMC_SetPositionCounter = lib.BMC_SetPositionCounter
BMC_SetPositionCounter.restype = c_short
BMC_SetPositionCounter.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    count = c_long()

    output = BMC_SetPositionCounter(serial_number)

    return output


BMC_SetRotationModes = lib.BMC_SetRotationModes
BMC_SetRotationModes.restype = c_short
BMC_SetRotationModes.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = BMC_SetRotationModes(serial_number)

    return output


BMC_SetStageAxisLimits = lib.BMC_SetStageAxisLimits
BMC_SetStageAxisLimits.restype = c_short
BMC_SetStageAxisLimits.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    minPosition = c_int()
    maxPosition = c_int()

    output = BMC_SetStageAxisLimits(serial_number)

    return output


BMC_SetTrackSettleParams = lib.BMC_SetTrackSettleParams
BMC_SetTrackSettleParams.restype = c_short
BMC_SetTrackSettleParams.argtypes = []


def set_track_settle_params(serial_number):
    '''
    Sets the track settled parameters used to decide when settled at right position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        settleParams: MOT_BrushlessTrackSettleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    settleParams = MOT_BrushlessTrackSettleParameters()

    output = BMC_SetTrackSettleParams(serial_number)

    return output


BMC_SetTriggerConfigParams = lib.BMC_SetTriggerConfigParams
BMC_SetTriggerConfigParams.restype = c_short
BMC_SetTriggerConfigParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    trigger1Mode = KMOT_TriggerPortMode()
    trigger1Polarity = KMOT_TriggerPortPolarity()
    trigger2Mode = KMOT_TriggerPortMode()
    trigger2Polarity = KMOT_TriggerPortPolarity()

    output = BMC_SetTriggerConfigParams(serial_number)

    return output


BMC_SetTriggerConfigParamsBlock = lib.BMC_SetTriggerConfigParamsBlock
BMC_SetTriggerConfigParamsBlock.restype = c_short
BMC_SetTriggerConfigParamsBlock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    triggerConfigParams = KMOT_TriggerConfig()

    output = BMC_SetTriggerConfigParamsBlock(serial_number)

    return output


BMC_SetTriggerParamsParams = lib.BMC_SetTriggerParamsParams
BMC_SetTriggerParamsParams.restype = c_short
BMC_SetTriggerParamsParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    triggerStartPositionFwd = c_int32()
    triggerIntervalFwd = c_int32()
    triggerPulseCountFwd = c_int32()
    triggerStartPositionRev = c_int32()
    triggerIntervalRev = c_int32()
    triggerPulseCountRev = c_int32()
    triggerPulseWidth = c_int32()
    cycleCount = c_int32()

    output = BMC_SetTriggerParamsParams(serial_number)

    return output


BMC_SetTriggerParamsParamsBlock = lib.BMC_SetTriggerParamsParamsBlock
BMC_SetTriggerParamsParamsBlock.restype = c_short
BMC_SetTriggerParamsParamsBlock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    triggerParamsParams = KMOT_TriggerParams()

    output = BMC_SetTriggerParamsParamsBlock(serial_number)

    return output


BMC_SetTriggerSwitches = lib.BMC_SetTriggerSwitches
BMC_SetTriggerSwitches.restype = c_short
BMC_SetTriggerSwitches.argtypes = []


def set_trigger_switches(serial_number):
    '''
    Sets the trigger switch bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        indicatorBits: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    indicatorBits = c_byte()

    output = BMC_SetTriggerSwitches(serial_number)

    return output


BMC_SetVelParams = lib.BMC_SetVelParams
BMC_SetVelParams.restype = c_short
BMC_SetVelParams.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    acceleration = c_int()
    maxVelocity = c_int()

    output = BMC_SetVelParams(serial_number)

    return output


BMC_SetVelParamsBlock = lib.BMC_SetVelParamsBlock
BMC_SetVelParamsBlock.restype = c_short
BMC_SetVelParamsBlock.argtypes = []


def set_vel_params_block(serial_number):
    '''
    Set the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocityParams: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocityParams = MOT_VelocityParameters()

    output = BMC_SetVelParamsBlock(serial_number)

    return output


BMC_SetVelocityProfileParams = lib.BMC_SetVelocityProfileParams
BMC_SetVelocityProfileParams.restype = c_short
BMC_SetVelocityProfileParams.argtypes = []


def set_velocity_profile_params(serial_number):
    '''
    Sets the velocity profile parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        velocityProfileParams: MOT_VelocityProfileParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    velocityProfileParams = MOT_VelocityProfileParameters()

    output = BMC_SetVelocityProfileParams(serial_number)

    return output


BMC_StartPolling = lib.BMC_StartPolling
BMC_StartPolling.restype = c_bool
BMC_StartPolling.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    milliseconds = c_int()

    output = BMC_StartPolling(serial_number)

    return output


BMC_StopImmediate = lib.BMC_StopImmediate
BMC_StopImmediate.restype = c_short
BMC_StopImmediate.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_StopImmediate(serial_number)

    return output


BMC_StopPolling = lib.BMC_StopPolling
BMC_StopPolling.restype = c_void_p
BMC_StopPolling.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_StopPolling(serial_number)

    return output


BMC_StopProfiled = lib.BMC_StopProfiled
BMC_StopProfiled.restype = c_short
BMC_StopProfiled.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_StopProfiled(serial_number)

    return output


BMC_SuspendMoveMessages = lib.BMC_SuspendMoveMessages
BMC_SuspendMoveMessages.restype = c_short
BMC_SuspendMoveMessages.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()

    output = BMC_SuspendMoveMessages(serial_number)

    return output


BMC_TimeSinceLastMsgReceived = lib.BMC_TimeSinceLastMsgReceived
BMC_TimeSinceLastMsgReceived.restype = c_bool
BMC_TimeSinceLastMsgReceived.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    lastUpdateTimeMS = c_int64()

    output = BMC_TimeSinceLastMsgReceived(serial_number)

    return output


BMC_WaitForMessage = lib.BMC_WaitForMessage
BMC_WaitForMessage.restype = c_bool
BMC_WaitForMessage.argtypes = []


def wait_for_message(serial_number):
    '''
    Wait for next MessageQueue item.

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

    serial_number = c_char_pointer(serial_number)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = BMC_WaitForMessage(serial_number)

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


