from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
    c_int,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    TIM_ButtonParameters,
    TIM_ButtonsMode,
    TIM_Channels,
    TIM_Direction,
    TIM_DriveOPParameters,
    TIM_JogMode,
    TIM_JogParameters)
from .definitions.structures import (
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
    lib_path + "Thorlabs.MotionControl.TCube.InertialMotor.DLL")

TIM_CheckConnection = lib.TIM_CheckConnection
TIM_CheckConnection.restype = c_bool
TIM_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = TIM_CheckConnection(serial_number)

    return output


TIM_ClearMessageQueue = lib.TIM_ClearMessageQueue
TIM_ClearMessageQueue.restype = c_void_p
TIM_ClearMessageQueue.argtypes = []


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

    output = TIM_ClearMessageQueue(serial_number)

    return output


TIM_Close = lib.TIM_Close
TIM_Close.restype = c_void_p
TIM_Close.argtypes = []


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

    output = TIM_Close(serial_number)

    return output


TIM_Disable = lib.TIM_Disable
TIM_Disable.restype = c_short
TIM_Disable.argtypes = []


def disable(serial_number):
    '''
    Disable cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_Disable(serial_number)

    return output


TIM_Disconnect = lib.TIM_Disconnect
TIM_Disconnect.restype = c_short
TIM_Disconnect.argtypes = []


def disconnect(serial_number):
    '''
    Tells the device that it is being disconnected.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_Disconnect(serial_number)

    return output


TIM_Enable = lib.TIM_Enable
TIM_Enable.restype = c_short
TIM_Enable.argtypes = []


def enable(serial_number):
    '''
    Enable cube for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_Enable(serial_number)

    return output


TIM_EnableLastMsgTimer = lib.TIM_EnableLastMsgTimer
TIM_EnableLastMsgTimer.restype = c_void_p
TIM_EnableLastMsgTimer.argtypes = []


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

    output = TIM_EnableLastMsgTimer(serial_number)

    return output


TIM_GetButtonParameters = lib.TIM_GetButtonParameters
TIM_GetButtonParameters.restype = c_short
TIM_GetButtonParameters.argtypes = []


def get_button_parameters(serial_number):
    '''
    Gets a button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        buttonMode: TIM_ButtonsMode
        position1: c_int32
        position2: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    buttonMode = TIM_ButtonsMode()
    position1 = c_int32()
    position2 = c_int32()

    output = TIM_GetButtonParameters(serial_number)

    return output


TIM_GetButtonParametersStruct = lib.TIM_GetButtonParametersStruct
TIM_GetButtonParametersStruct.restype = c_short
TIM_GetButtonParametersStruct.argtypes = []


def get_button_parameters_struct(serial_number):
    '''
    Gets a button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        buttonParameters: TIM_ButtonParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    buttonParameters = TIM_ButtonParameters()

    output = TIM_GetButtonParametersStruct(serial_number)

    return output


TIM_GetCurrentPosition = lib.TIM_GetCurrentPosition
TIM_GetCurrentPosition.restype = c_int32
TIM_GetCurrentPosition.argtypes = []


def get_current_position(serial_number):
    '''
    Gets current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_int32
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_GetCurrentPosition(serial_number)

    return output


TIM_GetDriveOPParameters = lib.TIM_GetDriveOPParameters
TIM_GetDriveOPParameters.restype = c_short
TIM_GetDriveOPParameters.argtypes = []


def get_drive_o_p_parameters(serial_number):
    '''
    Gets the operation drive parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        maxVoltage: c_int16
        stepRate: c_int32
        stepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    maxVoltage = c_int16()
    stepRate = c_int32()
    stepAcceleration = c_int32()

    output = TIM_GetDriveOPParameters(serial_number)

    return output


TIM_GetDriveOPParametersStruct = lib.TIM_GetDriveOPParametersStruct
TIM_GetDriveOPParametersStruct.restype = c_short
TIM_GetDriveOPParametersStruct.argtypes = []


def get_drive_o_p_parameters_struct(serial_number):
    '''
    Gets the operation drive parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        driveOPParameters: TIM_DriveOPParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    driveOPParameters = TIM_DriveOPParameters()

    output = TIM_GetDriveOPParametersStruct(serial_number)

    return output


TIM_GetFirmwareVersion = lib.TIM_GetFirmwareVersion
TIM_GetFirmwareVersion.restype = c_ulong
TIM_GetFirmwareVersion.argtypes = []


def get_firmware_version(serial_number):
    '''
    Gets version number of the device firmware.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_GetFirmwareVersion(serial_number)

    return output


TIM_GetHardwareInfo = lib.TIM_GetHardwareInfo
TIM_GetHardwareInfo.restype = c_short
TIM_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = TIM_GetHardwareInfo(serial_number)

    return output


TIM_GetHardwareInfoBlock = lib.TIM_GetHardwareInfoBlock
TIM_GetHardwareInfoBlock.restype = c_short
TIM_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = TIM_GetHardwareInfoBlock(serial_number)

    return output


TIM_GetJogParameters = lib.TIM_GetJogParameters
TIM_GetJogParameters.restype = c_short
TIM_GetJogParameters.argtypes = []


def get_jog_parameters(serial_number):
    '''
    Gets the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        jogMode: TIM_JogMode
        jogStepSize: c_int32
        jogStepRate: c_int32
        jogStepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    jogMode = TIM_JogMode()
    jogStepSize = c_int32()
    jogStepRate = c_int32()
    jogStepAcceleration = c_int32()

    output = TIM_GetJogParameters(serial_number)

    return output


TIM_GetJogParametersStruct = lib.TIM_GetJogParametersStruct
TIM_GetJogParametersStruct.restype = c_short
TIM_GetJogParametersStruct.argtypes = []


def get_jog_parameters_struct(serial_number):
    '''
    Gets the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        jogParameters: TIM_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    jogParameters = TIM_JogParameters()

    output = TIM_GetJogParametersStruct(serial_number)

    return output


TIM_GetLEDBrightness = lib.TIM_GetLEDBrightness
TIM_GetLEDBrightness.restype = c_short
TIM_GetLEDBrightness.argtypes = []


def get_l_e_d_brightness(serial_number):
    '''
    Gets the LED brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_GetLEDBrightness(serial_number)

    return output


TIM_GetMaxPotStepRate = lib.TIM_GetMaxPotStepRate
TIM_GetMaxPotStepRate.restype = c_int32
TIM_GetMaxPotStepRate.argtypes = []


def get_max_pot_step_rate(serial_number):
    '''
    Gets the maximum potentiometer step rate.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_int32
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_GetMaxPotStepRate(serial_number)

    return output


TIM_GetNextMessage = lib.TIM_GetNextMessage
TIM_GetNextMessage.restype = c_bool
TIM_GetNextMessage.argtypes = []


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

    output = TIM_GetNextMessage(serial_number)

    return output


TIM_GetSoftwareVersion = lib.TIM_GetSoftwareVersion
TIM_GetSoftwareVersion.restype = c_ulong
TIM_GetSoftwareVersion.argtypes = []


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

    output = TIM_GetSoftwareVersion(serial_number)

    return output


TIM_GetStatusBits = lib.TIM_GetStatusBits
TIM_GetStatusBits.restype = c_ulong
TIM_GetStatusBits.argtypes = []


def get_status_bits(serial_number):
    '''
    Tc get status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_GetStatusBits(serial_number)

    return output


TIM_HasLastMsgTimerOverrun = lib.TIM_HasLastMsgTimerOverrun
TIM_HasLastMsgTimerOverrun.restype = c_bool
TIM_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by TIM_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_HasLastMsgTimerOverrun(serial_number)

    return output


TIM_Home = lib.TIM_Home
TIM_Home.restype = c_short
TIM_Home.argtypes = []


def home(serial_number):
    '''
    Sets the current position to the Home position (Position = 0).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_Home(serial_number)

    return output


TIM_Identify = lib.TIM_Identify
TIM_Identify.restype = c_void_p
TIM_Identify.argtypes = []


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

    output = TIM_Identify(serial_number)

    return output


TIM_LoadNamedSettings = lib.TIM_LoadNamedSettings
TIM_LoadNamedSettings.restype = c_bool
TIM_LoadNamedSettings.argtypes = []


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

    output = TIM_LoadNamedSettings(serial_number)

    return output


TIM_LoadSettings = lib.TIM_LoadSettings
TIM_LoadSettings.restype = c_bool
TIM_LoadSettings.argtypes = []


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

    output = TIM_LoadSettings(serial_number)

    return output


TIM_MessageQueueSize = lib.TIM_MessageQueueSize
TIM_MessageQueueSize.restype = c_int
TIM_MessageQueueSize.argtypes = []


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

    output = TIM_MessageQueueSize(serial_number)

    return output


TIM_MoveAbsolute = lib.TIM_MoveAbsolute
TIM_MoveAbsolute.restype = c_short
TIM_MoveAbsolute.argtypes = []


def move_absolute(serial_number):
    '''
    Move absolute.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        position: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    position = c_int32()

    output = TIM_MoveAbsolute(serial_number)

    return output


TIM_MoveJog = lib.TIM_MoveJog
TIM_MoveJog.restype = c_short
TIM_MoveJog.argtypes = []


def move_jog(serial_number):
    '''
    Move jog.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        jogDirection: TIM_Direction

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    jogDirection = TIM_Direction()

    output = TIM_MoveJog(serial_number)

    return output


TIM_MoveStop = lib.TIM_MoveStop
TIM_MoveStop.restype = c_short
TIM_MoveStop.argtypes = []


def move_stop(serial_number):
    '''
    Move stop.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_MoveStop(serial_number)

    return output


TIM_Open = lib.TIM_Open
TIM_Open.restype = c_short
TIM_Open.argtypes = []


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

    output = TIM_Open(serial_number)

    return output


TIM_PersistSettings = lib.TIM_PersistSettings
TIM_PersistSettings.restype = c_bool
TIM_PersistSettings.argtypes = []


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

    output = TIM_PersistSettings(serial_number)

    return output


TIM_PollingDuration = lib.TIM_PollingDuration
TIM_PollingDuration.restype = c_long
TIM_PollingDuration.argtypes = []


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

    output = TIM_PollingDuration(serial_number)

    return output


TIM_RegisterMessageCallback = lib.TIM_RegisterMessageCallback
TIM_RegisterMessageCallback.restype = c_void_p
TIM_RegisterMessageCallback.argtypes = []


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

    output = TIM_RegisterMessageCallback(serial_number)

    return output


TIM_RequestButtonParameters = lib.TIM_RequestButtonParameters
TIM_RequestButtonParameters.restype = c_short
TIM_RequestButtonParameters.argtypes = []


def request_button_parameters(serial_number):
    '''
    Requests the button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_RequestButtonParameters(serial_number)

    return output


TIM_RequestCurrentPosition = lib.TIM_RequestCurrentPosition
TIM_RequestCurrentPosition.restype = c_short
TIM_RequestCurrentPosition.argtypes = []


def request_current_position(serial_number):
    '''
    Requests the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_RequestCurrentPosition(serial_number)

    return output


TIM_RequestDriveOPParameters = lib.TIM_RequestDriveOPParameters
TIM_RequestDriveOPParameters.restype = c_short
TIM_RequestDriveOPParameters.argtypes = []


def request_drive_o_p_parameters(serial_number):
    '''
    Requests the operation drive parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_RequestDriveOPParameters(serial_number)

    return output


TIM_RequestJogParameters = lib.TIM_RequestJogParameters
TIM_RequestJogParameters.restype = c_short
TIM_RequestJogParameters.argtypes = []


def request_jog_parameters(serial_number):
    '''
    Requests the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_RequestJogParameters(serial_number)

    return output


TIM_RequestMaxPotStepRate = lib.TIM_RequestMaxPotStepRate
TIM_RequestMaxPotStepRate.restype = c_short
TIM_RequestMaxPotStepRate.argtypes = []


def request_max_pot_step_rate(serial_number):
    '''
    Requests the maximum potentiometer step rate.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()

    output = TIM_RequestMaxPotStepRate(serial_number)

    return output


TIM_RequestSettings = lib.TIM_RequestSettings
TIM_RequestSettings.restype = c_short
TIM_RequestSettings.argtypes = []


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

    output = TIM_RequestSettings(serial_number)

    return output


TIM_RequestStatus = lib.TIM_RequestStatus
TIM_RequestStatus.restype = c_short
TIM_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Requests the state quantities (actual temperature, current and status bits).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_RequestStatus(serial_number)

    return output


TIM_RequestStatusBits = lib.TIM_RequestStatusBits
TIM_RequestStatusBits.restype = c_short
TIM_RequestStatusBits.argtypes = []


def request_status_bits(serial_number):
    '''
    Request the status bits which identify the current device state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_RequestStatusBits(serial_number)

    return output


TIM_Reset = lib.TIM_Reset
TIM_Reset.restype = c_short
TIM_Reset.argtypes = []


def reset(serial_number):
    '''
    Reset the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TIM_Reset(serial_number)

    return output


TIM_SetButtonParameters = lib.TIM_SetButtonParameters
TIM_SetButtonParameters.restype = c_short
TIM_SetButtonParameters.argtypes = []


def set_button_parameters(serial_number):
    '''
    Sets a button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        buttonMode: TIM_ButtonsMode
        position1: c_int32
        position2: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    buttonMode = TIM_ButtonsMode()
    position1 = c_int32()
    position2 = c_int32()

    output = TIM_SetButtonParameters(serial_number)

    return output


TIM_SetButtonParametersStruct = lib.TIM_SetButtonParametersStruct
TIM_SetButtonParametersStruct.restype = c_short
TIM_SetButtonParametersStruct.argtypes = []


def set_button_parameters_struct(serial_number):
    '''
    Sets a button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        buttonParameters: TIM_ButtonParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    buttonParameters = TIM_ButtonParameters()

    output = TIM_SetButtonParametersStruct(serial_number)

    return output


TIM_SetDriveOPParameters = lib.TIM_SetDriveOPParameters
TIM_SetDriveOPParameters.restype = c_short
TIM_SetDriveOPParameters.argtypes = []


def set_drive_o_p_parameters(serial_number):
    '''
    Sets the operation drive parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        maxVoltage: c_int16
        stepRate: c_int32
        stepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    maxVoltage = c_int16()
    stepRate = c_int32()
    stepAcceleration = c_int32()

    output = TIM_SetDriveOPParameters(serial_number)

    return output


TIM_SetDriveOPParametersStruct = lib.TIM_SetDriveOPParametersStruct
TIM_SetDriveOPParametersStruct.restype = c_short
TIM_SetDriveOPParametersStruct.argtypes = []


def set_drive_o_p_parameters_struct(serial_number):
    '''
    Sets the operation drive parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        driveOPParameters: TIM_DriveOPParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    driveOPParameters = TIM_DriveOPParameters()

    output = TIM_SetDriveOPParametersStruct(serial_number)

    return output


TIM_SetJogParameters = lib.TIM_SetJogParameters
TIM_SetJogParameters.restype = c_short
TIM_SetJogParameters.argtypes = []


def set_jog_parameters(serial_number):
    '''
    Sets the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        jogMode: TIM_JogMode
        jogStepSize: c_int32
        jogStepRate: c_int32
        jogStepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    jogMode = TIM_JogMode()
    jogStepSize = c_int32()
    jogStepRate = c_int32()
    jogStepAcceleration = c_int32()

    output = TIM_SetJogParameters(serial_number)

    return output


TIM_SetJogParametersStruct = lib.TIM_SetJogParametersStruct
TIM_SetJogParametersStruct.restype = c_short
TIM_SetJogParametersStruct.argtypes = []


def set_jog_parameters_struct(serial_number):
    '''
    Sets the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        jogParameters: TIM_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    jogParameters = TIM_JogParameters()

    output = TIM_SetJogParametersStruct(serial_number)

    return output


TIM_SetLEDBrightness = lib.TIM_SetLEDBrightness
TIM_SetLEDBrightness.restype = c_short
TIM_SetLEDBrightness.argtypes = []


def set_l_e_d_brightness(serial_number):
    '''
    Sets the LED brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        brightness: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    brightness = c_short()

    output = TIM_SetLEDBrightness(serial_number)

    return output


TIM_SetMaxPotStepRate = lib.TIM_SetMaxPotStepRate
TIM_SetMaxPotStepRate.restype = c_short
TIM_SetMaxPotStepRate.argtypes = []


def set_max_pot_step_rate(serial_number):
    '''
    Sets a maximum pot step rate.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        maxPotStepRate: c_int32

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    maxPotStepRate = c_int32()

    output = TIM_SetMaxPotStepRate(serial_number)

    return output


TIM_SetPosition = lib.TIM_SetPosition
TIM_SetPosition.restype = c_short
TIM_SetPosition.argtypes = []


def set_position(serial_number):
    '''
    set the position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: TIM_Channels
        position: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    channel = TIM_Channels()
    position = c_long()

    output = TIM_SetPosition(serial_number)

    return output


TIM_StartPolling = lib.TIM_StartPolling
TIM_StartPolling.restype = c_bool
TIM_StartPolling.argtypes = []


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

    output = TIM_StartPolling(serial_number)

    return output


TIM_StopPolling = lib.TIM_StopPolling
TIM_StopPolling.restype = c_void_p
TIM_StopPolling.argtypes = []


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

    output = TIM_StopPolling(serial_number)

    return output


TIM_TimeSinceLastMsgReceived = lib.TIM_TimeSinceLastMsgReceived
TIM_TimeSinceLastMsgReceived.restype = c_bool
TIM_TimeSinceLastMsgReceived.argtypes = []


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

    output = TIM_TimeSinceLastMsgReceived(serial_number)

    return output


TIM_WaitForMessage = lib.TIM_WaitForMessage
TIM_WaitForMessage.restype = c_bool
TIM_WaitForMessage.argtypes = []


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

    output = TIM_WaitForMessage(serial_number)

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


