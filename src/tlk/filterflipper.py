from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_uint, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (FF_Positions)
from .definitions.structures import (FF_IOSettings, TLI_DeviceInfo)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.FilterFlipper.DLL")

FF_CheckConnection = lib.FF_CheckConnection
FF_CheckConnection.restype = c_bool
FF_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = FF_CheckConnection(serial_number)

    return output


FF_ClearMessageQueue = lib.FF_ClearMessageQueue
FF_ClearMessageQueue.restype = c_void_p
FF_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = FF_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_Close = lib.FF_Close
FF_Close.restype = c_void_p
FF_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = FF_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_EnableLastMsgTimer = lib.FF_EnableLastMsgTimer
FF_EnableLastMsgTimer.restype = c_void_p
FF_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = FF_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


FF_GetFirmwareVersion = lib.FF_GetFirmwareVersion
FF_GetFirmwareVersion.restype = c_ulong
FF_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of firmware.

    serial_number = POINTER(c_char)

    output = FF_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_GetHardwareInfo = lib.FF_GetHardwareInfo
FF_GetHardwareInfo.restype = c_short
FF_GetHardwareInfo.argtypes = [
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

    output = FF_GetHardwareInfo(
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


FF_GetIOSettings = lib.FF_GetIOSettings
FF_GetIOSettings.restype = c_short
FF_GetIOSettings.argtypes = [POINTER(c_char), FF_IOSettings]


def get_i_o_settings(serial_number):
    # Gets the I/O settings from filter flipper.

    serial_number = POINTER(c_char)
    settings = FF_IOSettings()

    output = FF_GetIOSettings(serial_number, settings)
    if output != 0:
        raise KinesisException(output)


FF_GetNextMessage = lib.FF_GetNextMessage
FF_GetNextMessage.restype = c_bool
FF_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = FF_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


FF_GetNumberPositions = lib.FF_GetNumberPositions
FF_GetNumberPositions.restype = c_int
FF_GetNumberPositions.argtypes = [POINTER(c_char)]


def get_number_positions(serial_number):
    # Get number of positions.

    serial_number = POINTER(c_char)

    output = FF_GetNumberPositions(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_GetPosition = lib.FF_GetPosition
FF_GetPosition.restype = FF_Positions
FF_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)

    output = FF_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_GetSoftwareVersion = lib.FF_GetSoftwareVersion
FF_GetSoftwareVersion.restype = c_ulong
FF_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = FF_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_GetStatusBits = lib.FF_GetStatusBits
FF_GetStatusBits.restype = c_ulong
FF_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = FF_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_GetTransitTime = lib.FF_GetTransitTime
FF_GetTransitTime.restype = c_uint
FF_GetTransitTime.argtypes = [POINTER(c_char)]


def get_transit_time(serial_number):
    # Gets the transit time.

    serial_number = POINTER(c_char)

    output = FF_GetTransitTime(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_HasLastMsgTimerOverrun = lib.FF_HasLastMsgTimerOverrun
FF_HasLastMsgTimerOverrun.restype = c_bool
FF_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by FF_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = FF_HasLastMsgTimerOverrun(serial_number)

    return output


FF_Home = lib.FF_Home
FF_Home.restype = c_short
FF_Home.argtypes = [POINTER(c_char)]


def home(serial_number):
    # Home the device.

    serial_number = POINTER(c_char)

    output = FF_Home(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_Identify = lib.FF_Identify
FF_Identify.restype = c_void_p
FF_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = FF_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_LoadNamedSettings = lib.FF_LoadNamedSettings
FF_LoadNamedSettings.restype = c_bool
FF_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = FF_LoadNamedSettings(serial_number, settingsName)

    return output


FF_LoadSettings = lib.FF_LoadSettings
FF_LoadSettings.restype = c_bool
FF_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = FF_LoadSettings(serial_number)

    return output


FF_MessageQueueSize = lib.FF_MessageQueueSize
FF_MessageQueueSize.restype = c_int
FF_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = FF_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_MoveToPosition = lib.FF_MoveToPosition
FF_MoveToPosition.restype = c_short
FF_MoveToPosition.argtypes = [POINTER(c_char), FF_Positions]


def move_to_position(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    position = FF_Positions()

    output = FF_MoveToPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


FF_Open = lib.FF_Open
FF_Open.restype = c_short
FF_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = FF_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_PersistSettings = lib.FF_PersistSettings
FF_PersistSettings.restype = c_bool
FF_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # Persist the devices current settings.

    serial_number = POINTER(c_char)

    output = FF_PersistSettings(serial_number)

    return output


FF_PollingDuration = lib.FF_PollingDuration
FF_PollingDuration.restype = c_long
FF_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = FF_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_RegisterMessageCallback = lib.FF_RegisterMessageCallback
FF_RegisterMessageCallback.restype = c_void_p
FF_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = FF_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


FF_RequestIOSettings = lib.FF_RequestIOSettings
FF_RequestIOSettings.restype = c_short
FF_RequestIOSettings.argtypes = [POINTER(c_char)]


def request_i_o_settings(serial_number):
    # Requests the I/O settings from filter flipper.

    serial_number = POINTER(c_char)

    output = FF_RequestIOSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_RequestSettings = lib.FF_RequestSettings
FF_RequestSettings.restype = c_short
FF_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = FF_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_RequestStatus = lib.FF_RequestStatus
FF_RequestStatus.restype = c_short
FF_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Request status bits.

    serial_number = POINTER(c_char)

    output = FF_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_SetIOSettings = lib.FF_SetIOSettings
FF_SetIOSettings.restype = c_short
FF_SetIOSettings.argtypes = [POINTER(c_char), FF_IOSettings]


def set_i_o_settings(serial_number):
    # Sets the settings on filter flipper.

    serial_number = POINTER(c_char)
    settings = FF_IOSettings()

    output = FF_SetIOSettings(serial_number, settings)
    if output != 0:
        raise KinesisException(output)


FF_SetTransitTime = lib.FF_SetTransitTime
FF_SetTransitTime.restype = c_short
FF_SetTransitTime.argtypes = [POINTER(c_char), c_uint]


def set_transit_time(serial_number):
    # Sets the transit time.

    serial_number = POINTER(c_char)
    transitTime = c_uint()

    output = FF_SetTransitTime(serial_number, transitTime)
    if output != 0:
        raise KinesisException(output)


FF_StartPolling = lib.FF_StartPolling
FF_StartPolling.restype = c_bool
FF_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = FF_StartPolling(serial_number, milliseconds)

    return output


FF_StopPolling = lib.FF_StopPolling
FF_StopPolling.restype = c_void_p
FF_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = FF_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


FF_TimeSinceLastMsgReceived = lib.FF_TimeSinceLastMsgReceived
FF_TimeSinceLastMsgReceived.restype = c_bool
FF_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = FF_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


FF_WaitForMessage = lib.FF_WaitForMessage
FF_WaitForMessage.restype = c_bool
FF_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = FF_WaitForMessage(serial_number, messageType, messageID, messageData)

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
