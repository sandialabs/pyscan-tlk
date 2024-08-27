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
    SC_OperatingModes,
    SC_OperatingStates)
from .definitions.structures import (
    SC_CycleParameters,
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
    lib_path + "Thorlabs.MotionControl.TCube.Solenoid.DLL")

SC_CheckConnection = lib.SC_CheckConnection
SC_CheckConnection.restype = c_bool
SC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = SC_CheckConnection(serial_number)

    return output


SC_ClearMessageQueue = lib.SC_ClearMessageQueue
SC_ClearMessageQueue.restype = c_void_p
SC_ClearMessageQueue.argtypes = []


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

    output = SC_ClearMessageQueue(serial_number)

    return output


SC_Close = lib.SC_Close
SC_Close.restype = c_void_p
SC_Close.argtypes = []


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

    output = SC_Close(serial_number)

    return output


SC_EnableLastMsgTimer = lib.SC_EnableLastMsgTimer
SC_EnableLastMsgTimer.restype = c_void_p
SC_EnableLastMsgTimer.argtypes = []


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

    output = SC_EnableLastMsgTimer(serial_number)

    return output


SC_GetCycleParams = lib.SC_GetCycleParams
SC_GetCycleParams.restype = c_short
SC_GetCycleParams.argtypes = []


def get_cycle_params(serial_number):
    '''
    Gets the cycle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        onTime: c_uint
        pOpenTime: c_uint
        offTime: c_uint
        pClosedTime: c_uint
        numCycles: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    onTime = c_uint()
    pOpenTime = c_uint()
    offTime = c_uint()
    pClosedTime = c_uint()
    numCycles = c_uint()

    output = SC_GetCycleParams(serial_number)

    return output


SC_GetCycleParamsBlock = lib.SC_GetCycleParamsBlock
SC_GetCycleParamsBlock.restype = c_short
SC_GetCycleParamsBlock.argtypes = []


def get_cycle_params_block(serial_number):
    '''
    Gets the cycle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        cycleParams: SC_CycleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    cycleParams = SC_CycleParameters()

    output = SC_GetCycleParamsBlock(serial_number)

    return output


SC_GetHardwareInfo = lib.SC_GetHardwareInfo
SC_GetHardwareInfo.restype = c_short
SC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = SC_GetHardwareInfo(serial_number)

    return output


SC_GetHardwareInfoBlock = lib.SC_GetHardwareInfoBlock
SC_GetHardwareInfoBlock.restype = c_short
SC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = SC_GetHardwareInfoBlock(serial_number)

    return output


SC_GetHubBay = lib.SC_GetHubBay
SC_GetHubBay.restype = POINTER(c_char)
SC_GetHubBay.argtypes = []


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

    output = SC_GetHubBay(serial_number)

    return output


SC_GetLEDswitches = lib.SC_GetLEDswitches
SC_GetLEDswitches.restype = c_long
SC_GetLEDswitches.argtypes = []


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

    output = SC_GetLEDswitches(serial_number)

    return output


SC_GetNextMessage = lib.SC_GetNextMessage
SC_GetNextMessage.restype = c_bool
SC_GetNextMessage.argtypes = []


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

    output = SC_GetNextMessage(serial_number)

    return output


SC_GetOperatingMode = lib.SC_GetOperatingMode
SC_GetOperatingMode.restype = SC_OperatingModes
SC_GetOperatingMode.argtypes = []


def get_operating_mode(serial_number):
    '''
    Gets the Operating Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        SC_OperatingModes
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_GetOperatingMode(serial_number)

    return output


SC_GetOperatingState = lib.SC_GetOperatingState
SC_GetOperatingState.restype = SC_OperatingStates
SC_GetOperatingState.argtypes = []


def get_operating_state(serial_number):
    '''
    Gets the current operating state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        SC_OperatingStates
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_GetOperatingState(serial_number)

    return output


SC_GetSoftwareVersion = lib.SC_GetSoftwareVersion
SC_GetSoftwareVersion.restype = c_ulong
SC_GetSoftwareVersion.argtypes = []


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

    output = SC_GetSoftwareVersion(serial_number)

    return output


SC_GetSolenoidState = lib.SC_GetSolenoidState
SC_GetSolenoidState.restype = SC_SolenoidStates
SC_GetSolenoidState.argtypes = []


def get_solenoid_state(serial_number):
    '''
    Gets the current solenoid state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        SC_SolenoidStates
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_GetSolenoidState(serial_number)

    return output


SC_GetStatusBits = lib.SC_GetStatusBits
SC_GetStatusBits.restype = c_ulong
SC_GetStatusBits.argtypes = []


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

    output = SC_GetStatusBits(serial_number)

    return output


SC_HasLastMsgTimerOverrun = lib.SC_HasLastMsgTimerOverrun
SC_HasLastMsgTimerOverrun.restype = c_bool
SC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by SC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_HasLastMsgTimerOverrun(serial_number)

    return output


SC_Identify = lib.SC_Identify
SC_Identify.restype = c_void_p
SC_Identify.argtypes = []


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

    output = SC_Identify(serial_number)

    return output


SC_LoadNamedSettings = lib.SC_LoadNamedSettings
SC_LoadNamedSettings.restype = c_bool
SC_LoadNamedSettings.argtypes = []


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

    output = SC_LoadNamedSettings(serial_number)

    return output


SC_LoadSettings = lib.SC_LoadSettings
SC_LoadSettings.restype = c_bool
SC_LoadSettings.argtypes = []


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

    output = SC_LoadSettings(serial_number)

    return output


SC_MessageQueueSize = lib.SC_MessageQueueSize
SC_MessageQueueSize.restype = c_int
SC_MessageQueueSize.argtypes = []


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

    output = SC_MessageQueueSize(serial_number)

    return output


SC_Open = lib.SC_Open
SC_Open.restype = c_short
SC_Open.argtypes = []


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

    output = SC_Open(serial_number)

    return output


SC_PersistSettings = lib.SC_PersistSettings
SC_PersistSettings.restype = c_bool
SC_PersistSettings.argtypes = []


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

    output = SC_PersistSettings(serial_number)

    return output


SC_PollingDuration = lib.SC_PollingDuration
SC_PollingDuration.restype = c_long
SC_PollingDuration.argtypes = []


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

    output = SC_PollingDuration(serial_number)

    return output


SC_RegisterMessageCallback = lib.SC_RegisterMessageCallback
SC_RegisterMessageCallback.restype = c_void_p
SC_RegisterMessageCallback.argtypes = []


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

    output = SC_RegisterMessageCallback(serial_number)

    return output


SC_RequestCycleParams = lib.SC_RequestCycleParams
SC_RequestCycleParams.restype = c_short
SC_RequestCycleParams.argtypes = []


def request_cycle_params(serial_number):
    '''
    Requests the cycle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_RequestCycleParams(serial_number)

    return output


SC_RequestHubBay = lib.SC_RequestHubBay
SC_RequestHubBay.restype = c_short
SC_RequestHubBay.argtypes = []


def request_hub_bay(serial_number):
    '''
    Requests the hub bay number this device is fitted to.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_RequestHubBay(serial_number)

    return output


SC_RequestLEDswitches = lib.SC_RequestLEDswitches
SC_RequestLEDswitches.restype = c_short
SC_RequestLEDswitches.argtypes = []


def request_l_e_dswitches(serial_number):
    '''
    Requests the LED indicator bits on cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_RequestLEDswitches(serial_number)

    return output


SC_RequestOperatingMode = lib.SC_RequestOperatingMode
SC_RequestOperatingMode.restype = c_short
SC_RequestOperatingMode.argtypes = []


def request_operating_mode(serial_number):
    '''
    Requests the Operating Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_RequestOperatingMode(serial_number)

    return output


SC_RequestOperatingState = lib.SC_RequestOperatingState
SC_RequestOperatingState.restype = c_short
SC_RequestOperatingState.argtypes = []


def request_operating_state(serial_number):
    '''
    Requests the operating state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_RequestOperatingState(serial_number)

    return output


SC_RequestSettings = lib.SC_RequestSettings
SC_RequestSettings.restype = c_short
SC_RequestSettings.argtypes = []


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

    output = SC_RequestSettings(serial_number)

    return output


SC_RequestStatus = lib.SC_RequestStatus
SC_RequestStatus.restype = c_short
SC_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Requests the status from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = SC_RequestStatus(serial_number)

    return output


SC_RequestStatusBits = lib.SC_RequestStatusBits
SC_RequestStatusBits.restype = c_short
SC_RequestStatusBits.argtypes = []


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

    output = SC_RequestStatusBits(serial_number)

    return output


SC_SetCycleParams = lib.SC_SetCycleParams
SC_SetCycleParams.restype = c_short
SC_SetCycleParams.argtypes = []


def set_cycle_params(serial_number):
    '''
    Sets the cycle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        onTime: c_uint
        openTime: c_uint
        offTime: c_uint
        closedTime: c_uint
        numCycles: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    onTime = c_uint()
    openTime = c_uint()
    offTime = c_uint()
    closedTime = c_uint()
    numCycles = c_uint()

    output = SC_SetCycleParams(serial_number)

    return output


SC_SetCycleParamsBlock = lib.SC_SetCycleParamsBlock
SC_SetCycleParamsBlock.restype = c_short
SC_SetCycleParamsBlock.argtypes = []


def set_cycle_params_block(serial_number):
    '''
    Sets the cycle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        cycleParams: SC_CycleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    cycleParams = SC_CycleParameters()

    output = SC_SetCycleParamsBlock(serial_number)

    return output


SC_SetLEDswitches = lib.SC_SetLEDswitches
SC_SetLEDswitches.restype = c_short
SC_SetLEDswitches.argtypes = []


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

    output = SC_SetLEDswitches(serial_number)

    return output


SC_SetOperatingMode = lib.SC_SetOperatingMode
SC_SetOperatingMode.restype = c_short
SC_SetOperatingMode.argtypes = []


def set_operating_mode(serial_number):
    '''
    Sets the Operating Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: SC_OperatingModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = SC_OperatingModes()

    output = SC_SetOperatingMode(serial_number)

    return output


SC_SetOperatingState = lib.SC_SetOperatingState
SC_SetOperatingState.restype = c_short
SC_SetOperatingState.argtypes = []


def set_operating_state(serial_number):
    '''
    Sets the operating state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        state: SC_OperatingStates

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    state = SC_OperatingStates()

    output = SC_SetOperatingState(serial_number)

    return output


SC_StartPolling = lib.SC_StartPolling
SC_StartPolling.restype = c_bool
SC_StartPolling.argtypes = []


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

    output = SC_StartPolling(serial_number)

    return output


SC_StopPolling = lib.SC_StopPolling
SC_StopPolling.restype = c_void_p
SC_StopPolling.argtypes = []


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

    output = SC_StopPolling(serial_number)

    return output


SC_TimeSinceLastMsgReceived = lib.SC_TimeSinceLastMsgReceived
SC_TimeSinceLastMsgReceived.restype = c_bool
SC_TimeSinceLastMsgReceived.argtypes = []


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

    output = SC_TimeSinceLastMsgReceived(serial_number)

    return output


SC_WaitForMessage = lib.SC_WaitForMessage
SC_WaitForMessage.restype = c_bool
SC_WaitForMessage.argtypes = []


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

    output = SC_WaitForMessage(serial_number)

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


