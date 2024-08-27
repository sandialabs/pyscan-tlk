from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
    c_double,
    c_int,
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
    MOT_TravelDirection,
    POL_PaddleBits,
    POL_Paddles,
    PolarizerParameters)
from .definitions.structures import (
    TLI_DeviceInfo)
from .definitions.kinesisexception import KinesisException

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Polarizer.DLL")

MPC_CheckConnection = lib.MPC_CheckConnection
MPC_CheckConnection.restype = c_bool
MPC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = MPC_CheckConnection(serial_number)

    return output


MPC_ClearMessageQueue = lib.MPC_ClearMessageQueue
MPC_ClearMessageQueue.restype = c_void_p
MPC_ClearMessageQueue.argtypes = []


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

    output = MPC_ClearMessageQueue(serial_number)

    return output


MPC_Close = lib.MPC_Close
MPC_Close.restype = c_void_p
MPC_Close.argtypes = []


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

    output = MPC_Close(serial_number)

    return output


MPC_EnableLastMsgTimer = lib.MPC_EnableLastMsgTimer
MPC_EnableLastMsgTimer.restype = c_void_p
MPC_EnableLastMsgTimer.argtypes = []


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

    output = MPC_EnableLastMsgTimer(serial_number)

    return output


MPC_GetEnabledPaddles = lib.MPC_GetEnabledPaddles
MPC_GetEnabledPaddles.restype = POL_PaddleBits
MPC_GetEnabledPaddles.argtypes = []


def get_enabled_paddles(serial_number):
    '''
    Gets enabled paddles.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        POL_PaddleBits
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetEnabledPaddles(serial_number)

    return output


MPC_GetFirmwareVersion = lib.MPC_GetFirmwareVersion
MPC_GetFirmwareVersion.restype = c_ulong
MPC_GetFirmwareVersion.argtypes = []


def get_firmware_version(serial_number):
    '''
    Gets version number of firmware.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetFirmwareVersion(serial_number)

    return output


MPC_GetHardwareInfo = lib.MPC_GetHardwareInfo
MPC_GetHardwareInfo.restype = c_short
MPC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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
    numchannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = MPC_GetHardwareInfo(serial_number)

    return output


MPC_GetHomeOffset = lib.MPC_GetHomeOffset
MPC_GetHomeOffset.restype = c_double
MPC_GetHomeOffset.argtypes = []


def get_home_offset(serial_number):
    '''
    Gets home offset.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_double
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetHomeOffset(serial_number)

    return output


MPC_GetJogSize = lib.MPC_GetJogSize
MPC_GetJogSize.restype = c_double
MPC_GetJogSize.argtypes = []


def get_jog_size(serial_number):
    '''
    Gets step size.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles

    Returns
    -------
        c_double
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()

    output = MPC_GetJogSize(serial_number)

    return output


MPC_GetMaxTravel = lib.MPC_GetMaxTravel
MPC_GetMaxTravel.restype = c_double
MPC_GetMaxTravel.argtypes = []


def get_max_travel(serial_number):
    '''
    Get the maximum travel in encoder steps.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_double
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetMaxTravel(serial_number)

    return output


MPC_GetNextMessage = lib.MPC_GetNextMessage
MPC_GetNextMessage.restype = c_bool
MPC_GetNextMessage.argtypes = []


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

    output = MPC_GetNextMessage(serial_number)

    return output


MPC_GetPaddleCount = lib.MPC_GetPaddleCount
MPC_GetPaddleCount.restype = c_int
MPC_GetPaddleCount.argtypes = []


def get_paddle_count(serial_number):
    '''
    Get number of polarizer paddles.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetPaddleCount(serial_number)

    return output


MPC_GetPolParams = lib.MPC_GetPolParams
MPC_GetPolParams.restype = c_short
MPC_GetPolParams.argtypes = []


def get_pol_params(serial_number):
    '''
    Gets the polarizer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        polParams: PolarizerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    polParams = PolarizerParameters()

    output = MPC_GetPolParams(serial_number)

    return output


MPC_GetPosition = lib.MPC_GetPosition
MPC_GetPosition.restype = c_double
MPC_GetPosition.argtypes = []


def get_position(serial_number):
    '''
    Get the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles

    Returns
    -------
        c_double
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()

    output = MPC_GetPosition(serial_number)

    return output


MPC_GetSoftwareVersion = lib.MPC_GetSoftwareVersion
MPC_GetSoftwareVersion.restype = c_ulong
MPC_GetSoftwareVersion.argtypes = []


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

    output = MPC_GetSoftwareVersion(serial_number)

    return output


MPC_GetStatusBits = lib.MPC_GetStatusBits
MPC_GetStatusBits.restype = c_ulong
MPC_GetStatusBits.argtypes = []


def get_status_bits(serial_number):
    '''
    Get the current status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()

    output = MPC_GetStatusBits(serial_number)

    return output


MPC_GetStepsPerDegree = lib.MPC_GetStepsPerDegree
MPC_GetStepsPerDegree.restype = c_double
MPC_GetStepsPerDegree.argtypes = []


def get_steps_per_degree(serial_number):
    '''
    Get the Ratio of encoder steps per degree.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_double
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetStepsPerDegree(serial_number)

    return output


MPC_GetVelocity = lib.MPC_GetVelocity
MPC_GetVelocity.restype = c_short
MPC_GetVelocity.argtypes = []


def get_velocity(serial_number):
    '''
    Gets the velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_GetVelocity(serial_number)

    return output


MPC_HasLastMsgTimerOverrun = lib.MPC_HasLastMsgTimerOverrun
MPC_HasLastMsgTimerOverrun.restype = c_bool
MPC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by MPC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_HasLastMsgTimerOverrun(serial_number)

    return output


MPC_Home = lib.MPC_Home
MPC_Home.restype = c_short
MPC_Home.argtypes = []


def home(serial_number):
    '''
    Home the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()

    output = MPC_Home(serial_number)

    return output


MPC_Identify = lib.MPC_Identify
MPC_Identify.restype = c_void_p
MPC_Identify.argtypes = []


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

    output = MPC_Identify(serial_number)

    return output


MPC_IsPaddleEnabled = lib.MPC_IsPaddleEnabled
MPC_IsPaddleEnabled.restype = c_bool
MPC_IsPaddleEnabled.argtypes = []


def is_paddle_enabled(serial_number):
    '''
    Queries if a paddle is enabled.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()

    output = MPC_IsPaddleEnabled(serial_number)

    return output


MPC_Jog = lib.MPC_Jog
MPC_Jog.restype = c_short
MPC_Jog.argtypes = []


def jog(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles
        direction: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()
    direction = MOT_TravelDirection()

    output = MPC_Jog(serial_number)

    return output


MPC_LoadNamedSettings = lib.MPC_LoadNamedSettings
MPC_LoadNamedSettings.restype = c_bool
MPC_LoadNamedSettings.argtypes = []


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

    output = MPC_LoadNamedSettings(serial_number)

    return output


MPC_LoadSettings = lib.MPC_LoadSettings
MPC_LoadSettings.restype = c_bool
MPC_LoadSettings.argtypes = []


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

    output = MPC_LoadSettings(serial_number)

    return output


MPC_MessageQueueSize = lib.MPC_MessageQueueSize
MPC_MessageQueueSize.restype = c_int
MPC_MessageQueueSize.argtypes = []


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

    output = MPC_MessageQueueSize(serial_number)

    return output


MPC_MoveRelative = lib.MPC_MoveRelative
MPC_MoveRelative.restype = c_short
MPC_MoveRelative.argtypes = []


def move_relative(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles
        position: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()
    position = c_double()

    output = MPC_MoveRelative(serial_number)

    return output


MPC_MoveToPosition = lib.MPC_MoveToPosition
MPC_MoveToPosition.restype = c_short
MPC_MoveToPosition.argtypes = []


def move_to_position(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles
        position: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()
    position = c_double()

    output = MPC_MoveToPosition(serial_number)

    return output


MPC_Open = lib.MPC_Open
MPC_Open.restype = c_short
MPC_Open.argtypes = []


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

    output = MPC_Open(serial_number)

    return output


MPC_PersistSettings = lib.MPC_PersistSettings
MPC_PersistSettings.restype = c_bool
MPC_PersistSettings.argtypes = []


def persist_settings(serial_number):
    '''
    Persist the devices current settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_PersistSettings(serial_number)

    return output


MPC_PollingDuration = lib.MPC_PollingDuration
MPC_PollingDuration.restype = c_long
MPC_PollingDuration.argtypes = []


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

    output = MPC_PollingDuration(serial_number)

    return output


MPC_RegisterMessageCallback = lib.MPC_RegisterMessageCallback
MPC_RegisterMessageCallback.restype = c_void_p
MPC_RegisterMessageCallback.argtypes = []


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

    output = MPC_RegisterMessageCallback(serial_number)

    return output


MPC_RequestPolParams = lib.MPC_RequestPolParams
MPC_RequestPolParams.restype = c_short
MPC_RequestPolParams.argtypes = []


def request_pol_params(serial_number):
    '''
    Request polarizer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_RequestPolParams(serial_number)

    return output


MPC_RequestSettings = lib.MPC_RequestSettings
MPC_RequestSettings.restype = c_short
MPC_RequestSettings.argtypes = []


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

    output = MPC_RequestSettings(serial_number)

    return output


MPC_RequestStatus = lib.MPC_RequestStatus
MPC_RequestStatus.restype = c_short
MPC_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Request status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_RequestStatus(serial_number)

    return output


MPC_ResetParameters = lib.MPC_ResetParameters
MPC_ResetParameters.restype = c_bool
MPC_ResetParameters.argtypes = []


def reset_parameters(serial_number):
    '''
    Mpc reset parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = MPC_ResetParameters(serial_number)

    return output


MPC_SetEnabledPaddles = lib.MPC_SetEnabledPaddles
MPC_SetEnabledPaddles.restype = c_int
MPC_SetEnabledPaddles.argtypes = []


def set_enabled_paddles(serial_number):
    '''
    Enables the specified paddles.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddles: POL_PaddleBits

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)
    paddles = POL_PaddleBits()

    output = MPC_SetEnabledPaddles(serial_number)

    return output


MPC_SetHomeOffset = lib.MPC_SetHomeOffset
MPC_SetHomeOffset.restype = c_short
MPC_SetHomeOffset.argtypes = []


def set_home_offset(serial_number):
    '''
    Sets home offset.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        homeOffset: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    homeOffset = c_double()

    output = MPC_SetHomeOffset(serial_number)

    return output


MPC_SetJogSize = lib.MPC_SetJogSize
MPC_SetJogSize.restype = c_short
MPC_SetJogSize.argtypes = []


def set_jog_size(serial_number):
    '''
    Sets jog size.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles
        jogSize: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()
    jogSize = c_double()

    output = MPC_SetJogSize(serial_number)

    return output


MPC_SetPolParams = lib.MPC_SetPolParams
MPC_SetPolParams.restype = c_short
MPC_SetPolParams.argtypes = []


def set_pol_params(serial_number):
    '''
    Gets the polarizer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        polParams: PolarizerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    polParams = PolarizerParameters()

    output = MPC_SetPolParams(serial_number)

    return output


MPC_SetVelocity = lib.MPC_SetVelocity
MPC_SetVelocity.restype = c_short
MPC_SetVelocity.argtypes = []


def set_velocity(serial_number):
    '''
    Sets a velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocity: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocity = c_short()

    output = MPC_SetVelocity(serial_number)

    return output


MPC_StartPolling = lib.MPC_StartPolling
MPC_StartPolling.restype = c_bool
MPC_StartPolling.argtypes = []


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

    output = MPC_StartPolling(serial_number)

    return output


MPC_Stop = lib.MPC_Stop
MPC_Stop.restype = c_short
MPC_Stop.argtypes = []


def stop(serial_number):
    '''
    Stop the device .

    Parameters
    ----------
        serial_number: POINTER(c_char)
        paddle: POL_Paddles

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    paddle = POL_Paddles()

    output = MPC_Stop(serial_number)

    return output


MPC_StopPolling = lib.MPC_StopPolling
MPC_StopPolling.restype = c_void_p
MPC_StopPolling.argtypes = []


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

    output = MPC_StopPolling(serial_number)

    return output


MPC_TimeSinceLastMsgReceived = lib.MPC_TimeSinceLastMsgReceived
MPC_TimeSinceLastMsgReceived.restype = c_bool
MPC_TimeSinceLastMsgReceived.argtypes = []


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

    output = MPC_TimeSinceLastMsgReceived(serial_number)

    return output


MPC_WaitForMessage = lib.MPC_WaitForMessage
MPC_WaitForMessage.restype = c_bool
MPC_WaitForMessage.argtypes = []


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

    output = MPC_WaitForMessage(serial_number)

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


