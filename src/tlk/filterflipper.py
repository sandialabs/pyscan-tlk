from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
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
    FF_Positions)
from .definitions.structures import (
    FF_IOSettings,
    TLI_DeviceInfo)
from .definitions.kinesisexception import KinesisException

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.FilterFlipper.DLL")

FF_CheckConnection = lib.FF_CheckConnection
FF_CheckConnection.restype = c_bool
FF_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = FF_CheckConnection(serial_number)

    return output


FF_ClearMessageQueue = lib.FF_ClearMessageQueue
FF_ClearMessageQueue.restype = c_void_p
FF_ClearMessageQueue.argtypes = []


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

    output = FF_ClearMessageQueue(serial_number)

    return output


FF_Close = lib.FF_Close
FF_Close.restype = c_void_p
FF_Close.argtypes = []


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

    output = FF_Close(serial_number)

    return output


FF_EnableLastMsgTimer = lib.FF_EnableLastMsgTimer
FF_EnableLastMsgTimer.restype = c_void_p
FF_EnableLastMsgTimer.argtypes = []


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

    output = FF_EnableLastMsgTimer(serial_number)

    return output


FF_GetFirmwareVersion = lib.FF_GetFirmwareVersion
FF_GetFirmwareVersion.restype = c_ulong
FF_GetFirmwareVersion.argtypes = []


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

    output = FF_GetFirmwareVersion(serial_number)

    return output


FF_GetHardwareInfo = lib.FF_GetHardwareInfo
FF_GetHardwareInfo.restype = c_short
FF_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = FF_GetHardwareInfo(serial_number)

    return output


FF_GetIOSettings = lib.FF_GetIOSettings
FF_GetIOSettings.restype = c_short
FF_GetIOSettings.argtypes = []


def get_i_o_settings(serial_number):
    '''
    Gets the I/O settings from filter flipper.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        settings: FF_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    settings = FF_IOSettings()

    output = FF_GetIOSettings(serial_number)

    return output


FF_GetNextMessage = lib.FF_GetNextMessage
FF_GetNextMessage.restype = c_bool
FF_GetNextMessage.argtypes = []


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

    output = FF_GetNextMessage(serial_number)

    return output


FF_GetNumberPositions = lib.FF_GetNumberPositions
FF_GetNumberPositions.restype = c_int
FF_GetNumberPositions.argtypes = []


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

    output = FF_GetNumberPositions(serial_number)

    return output


FF_GetPosition = lib.FF_GetPosition
FF_GetPosition.restype = FF_Positions
FF_GetPosition.argtypes = []


def get_position(serial_number):
    '''
    Get the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        FF_Positions
    '''

    serial_number = c_char_pointer(serial_number)

    output = FF_GetPosition(serial_number)

    return output


FF_GetSoftwareVersion = lib.FF_GetSoftwareVersion
FF_GetSoftwareVersion.restype = c_ulong
FF_GetSoftwareVersion.argtypes = []


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

    output = FF_GetSoftwareVersion(serial_number)

    return output


FF_GetStatusBits = lib.FF_GetStatusBits
FF_GetStatusBits.restype = c_ulong
FF_GetStatusBits.argtypes = []


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

    output = FF_GetStatusBits(serial_number)

    return output


FF_GetTransitTime = lib.FF_GetTransitTime
FF_GetTransitTime.restype = c_uint
FF_GetTransitTime.argtypes = []


def get_transit_time(serial_number):
    '''
    Gets the transit time.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)

    output = FF_GetTransitTime(serial_number)

    return output


FF_HasLastMsgTimerOverrun = lib.FF_HasLastMsgTimerOverrun
FF_HasLastMsgTimerOverrun.restype = c_bool
FF_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by FF_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = FF_HasLastMsgTimerOverrun(serial_number)

    return output


FF_Home = lib.FF_Home
FF_Home.restype = c_short
FF_Home.argtypes = []


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

    output = FF_Home(serial_number)

    return output


FF_Identify = lib.FF_Identify
FF_Identify.restype = c_void_p
FF_Identify.argtypes = []


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

    output = FF_Identify(serial_number)

    return output


FF_LoadNamedSettings = lib.FF_LoadNamedSettings
FF_LoadNamedSettings.restype = c_bool
FF_LoadNamedSettings.argtypes = []


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

    output = FF_LoadNamedSettings(serial_number)

    return output


FF_LoadSettings = lib.FF_LoadSettings
FF_LoadSettings.restype = c_bool
FF_LoadSettings.argtypes = []


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

    output = FF_LoadSettings(serial_number)

    return output


FF_MessageQueueSize = lib.FF_MessageQueueSize
FF_MessageQueueSize.restype = c_int
FF_MessageQueueSize.argtypes = []


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

    output = FF_MessageQueueSize(serial_number)

    return output


FF_MoveToPosition = lib.FF_MoveToPosition
FF_MoveToPosition.restype = c_short
FF_MoveToPosition.argtypes = []


def move_to_position(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: FF_Positions

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    position = FF_Positions()

    output = FF_MoveToPosition(serial_number)

    return output


FF_Open = lib.FF_Open
FF_Open.restype = c_short
FF_Open.argtypes = []


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

    output = FF_Open(serial_number)

    return output


FF_PersistSettings = lib.FF_PersistSettings
FF_PersistSettings.restype = c_bool
FF_PersistSettings.argtypes = []


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

    output = FF_PersistSettings(serial_number)

    return output


FF_PollingDuration = lib.FF_PollingDuration
FF_PollingDuration.restype = c_long
FF_PollingDuration.argtypes = []


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

    output = FF_PollingDuration(serial_number)

    return output


FF_RegisterMessageCallback = lib.FF_RegisterMessageCallback
FF_RegisterMessageCallback.restype = c_void_p
FF_RegisterMessageCallback.argtypes = []


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

    output = FF_RegisterMessageCallback(serial_number)

    return output


FF_RequestIOSettings = lib.FF_RequestIOSettings
FF_RequestIOSettings.restype = c_short
FF_RequestIOSettings.argtypes = []


def request_i_o_settings(serial_number):
    '''
    Requests the I/O settings from filter flipper.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = FF_RequestIOSettings(serial_number)

    return output


FF_RequestSettings = lib.FF_RequestSettings
FF_RequestSettings.restype = c_short
FF_RequestSettings.argtypes = []


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

    output = FF_RequestSettings(serial_number)

    return output


FF_RequestStatus = lib.FF_RequestStatus
FF_RequestStatus.restype = c_short
FF_RequestStatus.argtypes = []


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

    output = FF_RequestStatus(serial_number)

    return output


FF_SetIOSettings = lib.FF_SetIOSettings
FF_SetIOSettings.restype = c_short
FF_SetIOSettings.argtypes = []


def set_i_o_settings(serial_number):
    '''
    Sets the settings on filter flipper.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        settings: FF_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    settings = FF_IOSettings()

    output = FF_SetIOSettings(serial_number)

    return output


FF_SetTransitTime = lib.FF_SetTransitTime
FF_SetTransitTime.restype = c_short
FF_SetTransitTime.argtypes = []


def set_transit_time(serial_number):
    '''
    Sets the transit time.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        transitTime: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    transitTime = c_uint()

    output = FF_SetTransitTime(serial_number)

    return output


FF_StartPolling = lib.FF_StartPolling
FF_StartPolling.restype = c_bool
FF_StartPolling.argtypes = []


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

    output = FF_StartPolling(serial_number)

    return output


FF_StopPolling = lib.FF_StopPolling
FF_StopPolling.restype = c_void_p
FF_StopPolling.argtypes = []


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

    output = FF_StopPolling(serial_number)

    return output


FF_TimeSinceLastMsgReceived = lib.FF_TimeSinceLastMsgReceived
FF_TimeSinceLastMsgReceived.restype = c_bool
FF_TimeSinceLastMsgReceived.argtypes = []


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

    output = FF_TimeSinceLastMsgReceived(serial_number)

    return output


FF_WaitForMessage = lib.FF_WaitForMessage
FF_WaitForMessage.restype = c_bool
FF_WaitForMessage.argtypes = []


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

    output = FF_WaitForMessage(serial_number)

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


