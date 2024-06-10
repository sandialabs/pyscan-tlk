from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_uint, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (SC_OperatingModes, SC_OperatingStates, SC_SolenoidStates)
from .definitions.structures import (SC_CycleParameters, TLI_DeviceInfo, TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.Solenoid.DLL")

SC_CheckConnection = lib.SC_CheckConnection
SC_CheckConnection.restype = c_bool
SC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = SC_CheckConnection(serial_number)

    return output


SC_ClearMessageQueue = lib.SC_ClearMessageQueue
SC_ClearMessageQueue.restype = c_void_p
SC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = SC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_Close = lib.SC_Close
SC_Close.restype = c_void_p
SC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = SC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_EnableLastMsgTimer = lib.SC_EnableLastMsgTimer
SC_EnableLastMsgTimer.restype = c_void_p
SC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


SC_GetCycleParams = lib.SC_GetCycleParams
SC_GetCycleParams.restype = c_short
SC_GetCycleParams.argtypes = [POINTER(c_char), c_uint, c_uint, c_uint, c_uint, c_uint]


def get_cycle_params(serial_number):
    # Gets the cycle parameters.

    serial_number = POINTER(c_char)
    onTime = c_uint()
    pOpenTime = c_uint()
    offTime = c_uint()
    pClosedTime = c_uint()
    numCycles = c_uint()

    output = SC_GetCycleParams(serial_number, onTime, pOpenTime, offTime, pClosedTime, numCycles)
    if output != 0:
        raise KinesisException(output)


SC_GetCycleParamsBlock = lib.SC_GetCycleParamsBlock
SC_GetCycleParamsBlock.restype = c_short
SC_GetCycleParamsBlock.argtypes = [POINTER(c_char), SC_CycleParameters]


def get_cycle_params_block(serial_number):
    # Gets the cycle parameters.

    serial_number = POINTER(c_char)
    cycleParams = SC_CycleParameters()

    output = SC_GetCycleParamsBlock(serial_number, cycleParams)
    if output != 0:
        raise KinesisException(output)


SC_GetHardwareInfo = lib.SC_GetHardwareInfo
SC_GetHardwareInfo.restype = c_short
SC_GetHardwareInfo.argtypes = [
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

    output = SC_GetHardwareInfo(
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


SC_GetHardwareInfoBlock = lib.SC_GetHardwareInfoBlock
SC_GetHardwareInfoBlock.restype = c_short
SC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = SC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


SC_GetHubBay = lib.SC_GetHubBay
SC_GetHubBay.restype = POINTER(c_char)
SC_GetHubBay.argtypes = [POINTER(c_char)]


def get_hub_bay(serial_number):
    # Gets the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = SC_GetHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_GetLEDswitches = lib.SC_GetLEDswitches
SC_GetLEDswitches.restype = c_long
SC_GetLEDswitches.argtypes = [POINTER(c_char)]


def get_l_e_dswitches(serial_number):
    # Get the LED indicator bits on cube.

    serial_number = POINTER(c_char)

    output = SC_GetLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_GetNextMessage = lib.SC_GetNextMessage
SC_GetNextMessage.restype = c_bool
SC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


SC_GetOperatingMode = lib.SC_GetOperatingMode
SC_GetOperatingMode.restype = SC_OperatingModes
SC_GetOperatingMode.argtypes = [POINTER(c_char)]


def get_operating_mode(serial_number):
    # Gets the Operating Mode.

    serial_number = POINTER(c_char)

    output = SC_GetOperatingMode(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_GetOperatingState = lib.SC_GetOperatingState
SC_GetOperatingState.restype = SC_OperatingStates
SC_GetOperatingState.argtypes = [POINTER(c_char)]


def get_operating_state(serial_number):
    # Gets the current operating state.

    serial_number = POINTER(c_char)

    output = SC_GetOperatingState(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_GetSoftwareVersion = lib.SC_GetSoftwareVersion
SC_GetSoftwareVersion.restype = c_ulong
SC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = SC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_GetSolenoidState = lib.SC_GetSolenoidState
SC_GetSolenoidState.restype = SC_SolenoidStates
SC_GetSolenoidState.argtypes = [POINTER(c_char)]


def get_solenoid_state(serial_number):
    # Gets the current solenoid state.

    serial_number = POINTER(c_char)

    output = SC_GetSolenoidState(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_GetStatusBits = lib.SC_GetStatusBits
SC_GetStatusBits.restype = c_ulong
SC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = SC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_HasLastMsgTimerOverrun = lib.SC_HasLastMsgTimerOverrun
SC_HasLastMsgTimerOverrun.restype = c_bool
SC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by SC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = SC_HasLastMsgTimerOverrun(serial_number)

    return output


SC_Identify = lib.SC_Identify
SC_Identify.restype = c_void_p
SC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = SC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_LoadNamedSettings = lib.SC_LoadNamedSettings
SC_LoadNamedSettings.restype = c_bool
SC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = SC_LoadNamedSettings(serial_number, settingsName)

    return output


SC_LoadSettings = lib.SC_LoadSettings
SC_LoadSettings.restype = c_bool
SC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = SC_LoadSettings(serial_number)

    return output


SC_MessageQueueSize = lib.SC_MessageQueueSize
SC_MessageQueueSize.restype = c_int
SC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = SC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_Open = lib.SC_Open
SC_Open.restype = c_short
SC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = SC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_PersistSettings = lib.SC_PersistSettings
SC_PersistSettings.restype = c_bool
SC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = SC_PersistSettings(serial_number)

    return output


SC_PollingDuration = lib.SC_PollingDuration
SC_PollingDuration.restype = c_long
SC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = SC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RegisterMessageCallback = lib.SC_RegisterMessageCallback
SC_RegisterMessageCallback.restype = c_void_p
SC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = SC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


SC_RequestCycleParams = lib.SC_RequestCycleParams
SC_RequestCycleParams.restype = c_short
SC_RequestCycleParams.argtypes = [POINTER(c_char)]


def request_cycle_params(serial_number):
    # Requests the cycle parameters.

    serial_number = POINTER(c_char)

    output = SC_RequestCycleParams(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestHubBay = lib.SC_RequestHubBay
SC_RequestHubBay.restype = c_short
SC_RequestHubBay.argtypes = [POINTER(c_char)]


def request_hub_bay(serial_number):
    # Requests the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = SC_RequestHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestLEDswitches = lib.SC_RequestLEDswitches
SC_RequestLEDswitches.restype = c_short
SC_RequestLEDswitches.argtypes = [POINTER(c_char)]


def request_l_e_dswitches(serial_number):
    # Requests the LED indicator bits on cube.

    serial_number = POINTER(c_char)

    output = SC_RequestLEDswitches(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestOperatingMode = lib.SC_RequestOperatingMode
SC_RequestOperatingMode.restype = c_short
SC_RequestOperatingMode.argtypes = [POINTER(c_char)]


def request_operating_mode(serial_number):
    # Requests the Operating Mode.

    serial_number = POINTER(c_char)

    output = SC_RequestOperatingMode(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestOperatingState = lib.SC_RequestOperatingState
SC_RequestOperatingState.restype = c_short
SC_RequestOperatingState.argtypes = [POINTER(c_char)]


def request_operating_state(serial_number):
    # Requests the operating state.

    serial_number = POINTER(c_char)

    output = SC_RequestOperatingState(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestSettings = lib.SC_RequestSettings
SC_RequestSettings.restype = c_short
SC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = SC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestStatus = lib.SC_RequestStatus
SC_RequestStatus.restype = c_short
SC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status from the device.

    serial_number = POINTER(c_char)

    output = SC_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_RequestStatusBits = lib.SC_RequestStatusBits
SC_RequestStatusBits.restype = c_short
SC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = SC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_SetCycleParams = lib.SC_SetCycleParams
SC_SetCycleParams.restype = c_short
SC_SetCycleParams.argtypes = [POINTER(c_char), c_uint, c_uint, c_uint, c_uint, c_uint]


def set_cycle_params(serial_number):
    # Sets the cycle parameters.

    serial_number = POINTER(c_char)
    onTime = c_uint()
    openTime = c_uint()
    offTime = c_uint()
    closedTime = c_uint()
    numCycles = c_uint()

    output = SC_SetCycleParams(serial_number, onTime, openTime, offTime, closedTime, numCycles)
    if output != 0:
        raise KinesisException(output)


SC_SetCycleParamsBlock = lib.SC_SetCycleParamsBlock
SC_SetCycleParamsBlock.restype = c_short
SC_SetCycleParamsBlock.argtypes = [POINTER(c_char), SC_CycleParameters]


def set_cycle_params_block(serial_number):
    # Sets the cycle parameters.

    serial_number = POINTER(c_char)
    cycleParams = SC_CycleParameters()

    output = SC_SetCycleParamsBlock(serial_number, cycleParams)
    if output != 0:
        raise KinesisException(output)


SC_SetLEDswitches = lib.SC_SetLEDswitches
SC_SetLEDswitches.restype = c_short
SC_SetLEDswitches.argtypes = [POINTER(c_char), c_long]


def set_l_e_dswitches(serial_number):
    # Set the LED indicator bits on cube.

    serial_number = POINTER(c_char)
    LEDswitches = c_long()

    output = SC_SetLEDswitches(serial_number, LEDswitches)
    if output != 0:
        raise KinesisException(output)


SC_SetOperatingMode = lib.SC_SetOperatingMode
SC_SetOperatingMode.restype = c_short
SC_SetOperatingMode.argtypes = [POINTER(c_char), SC_OperatingModes]


def set_operating_mode(serial_number):
    # Sets the Operating Mode.

    serial_number = POINTER(c_char)
    mode = SC_OperatingModes()

    output = SC_SetOperatingMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


SC_SetOperatingState = lib.SC_SetOperatingState
SC_SetOperatingState.restype = c_short
SC_SetOperatingState.argtypes = [POINTER(c_char), SC_OperatingStates]


def set_operating_state(serial_number):
    # Sets the operating state.

    serial_number = POINTER(c_char)
    state = SC_OperatingStates()

    output = SC_SetOperatingState(serial_number, state)
    if output != 0:
        raise KinesisException(output)


SC_StartPolling = lib.SC_StartPolling
SC_StartPolling.restype = c_bool
SC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = SC_StartPolling(serial_number, milliseconds)

    return output


SC_StopPolling = lib.SC_StopPolling
SC_StopPolling.restype = c_void_p
SC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = SC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


SC_TimeSinceLastMsgReceived = lib.SC_TimeSinceLastMsgReceived
SC_TimeSinceLastMsgReceived.restype = c_bool
SC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = SC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


SC_WaitForMessage = lib.SC_WaitForMessage
SC_WaitForMessage.restype = c_bool
SC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SC_WaitForMessage(serial_number, messageType, messageID, messageData)

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
