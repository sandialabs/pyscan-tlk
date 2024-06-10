from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_uint, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (TSG_Display_Modes, TSG_Hub_Analogue_Modes)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation, TSG_IOSettings)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.StrainGauge.DLL")

SG_CheckConnection = lib.SG_CheckConnection
SG_CheckConnection.restype = c_bool
SG_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = SG_CheckConnection(serial_number)

    return output


SG_ClearMessageQueue = lib.SG_ClearMessageQueue
SG_ClearMessageQueue.restype = c_void_p
SG_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = SG_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_Close = lib.SG_Close
SG_Close.restype = c_void_p
SG_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = SG_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_Disable = lib.SG_Disable
SG_Disable.restype = c_short
SG_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable the device.

    serial_number = POINTER(c_char)

    output = SG_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_Disconnect = lib.SG_Disconnect
SG_Disconnect.restype = c_short
SG_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = SG_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_Enable = lib.SG_Enable
SG_Enable.restype = c_short
SG_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable device for computer control.

    serial_number = POINTER(c_char)

    output = SG_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_EnableLastMsgTimer = lib.SG_EnableLastMsgTimer
SG_EnableLastMsgTimer.restype = c_void_p
SG_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = SG_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


SG_GetDisplayMode = lib.SG_GetDisplayMode
SG_GetDisplayMode.restype = TSG_Display_Modes
SG_GetDisplayMode.argtypes = [POINTER(c_char)]


def get_display_mode(serial_number):
    # Gets the display mode.

    serial_number = POINTER(c_char)

    output = SG_GetDisplayMode(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetFirmwareVersion = lib.SG_GetFirmwareVersion
SG_GetFirmwareVersion.restype = c_ulong
SG_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = SG_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetForceCalib = lib.SG_GetForceCalib
SG_GetForceCalib.restype = c_uint
SG_GetForceCalib.argtypes = [POINTER(c_char)]


def get_force_calib(serial_number):
    # Gets the maximum force in calibration.

    serial_number = POINTER(c_char)

    output = SG_GetForceCalib(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetHardwareInfo = lib.SG_GetHardwareInfo
SG_GetHardwareInfo.restype = c_short
SG_GetHardwareInfo.argtypes = [
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

    output = SG_GetHardwareInfo(
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


SG_GetHardwareInfoBlock = lib.SG_GetHardwareInfoBlock
SG_GetHardwareInfoBlock.restype = c_short
SG_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = SG_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


SG_GetHubAnalogOutput = lib.SG_GetHubAnalogOutput
SG_GetHubAnalogOutput.restype = TSG_Hub_Analogue_Modes
SG_GetHubAnalogOutput.argtypes = [POINTER(c_char)]


def get_hub_analog_output(serial_number):
    # Gets the Hub Analog Output.

    serial_number = POINTER(c_char)

    output = SG_GetHubAnalogOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetHubBay = lib.SG_GetHubBay
SG_GetHubBay.restype = POINTER(c_char)
SG_GetHubBay.argtypes = [POINTER(c_char)]


def get_hub_bay(serial_number):
    # Gets the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = SG_GetHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetIOsettingsBlock = lib.SG_GetIOsettingsBlock
SG_GetIOsettingsBlock.restype = c_short
SG_GetIOsettingsBlock.argtypes = [POINTER(c_char), TSG_IOSettings]


def get_i_osettings_block(serial_number):
    # Gets the input/output settings in a block.

    serial_number = POINTER(c_char)
    inputOutputSettings = TSG_IOSettings()

    output = SG_GetIOsettingsBlock(serial_number, inputOutputSettings)
    if output != 0:
        raise KinesisException(output)


SG_GetLEDBrightness = lib.SG_GetLEDBrightness
SG_GetLEDBrightness.restype = c_short
SG_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = SG_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetMaximumTravel = lib.SG_GetMaximumTravel
SG_GetMaximumTravel.restype = c_long
SG_GetMaximumTravel.argtypes = [POINTER(c_char)]


def get_maximum_travel(serial_number):
    # Gets the maximum travel of the strain gauge.

    serial_number = POINTER(c_char)

    output = SG_GetMaximumTravel(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetNextMessage = lib.SG_GetNextMessage
SG_GetNextMessage.restype = c_bool
SG_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SG_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


SG_GetReading = lib.SG_GetReading
SG_GetReading.restype = c_short
SG_GetReading.argtypes = [POINTER(c_char), c_bool]


def get_reading(serial_number):
    # Gets the current reading.

    serial_number = POINTER(c_char)
    smoothed = c_bool()

    output = SG_GetReading(serial_number, smoothed)
    if output != 0:
        raise KinesisException(output)


SG_GetReadingExt = lib.SG_GetReadingExt
SG_GetReadingExt.restype = c_int
SG_GetReadingExt.argtypes = [POINTER(c_char), c_bool, c_bool]


def get_reading_ext(serial_number):
    # Gets the current reading.

    serial_number = POINTER(c_char)
    clipReadng = c_bool()
    overrange = c_bool()

    output = SG_GetReadingExt(serial_number, clipReadng, overrange)
    if output != 0:
        raise KinesisException(output)


SG_GetSoftwareVersion = lib.SG_GetSoftwareVersion
SG_GetSoftwareVersion.restype = c_ulong
SG_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = SG_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_GetStatusBits = lib.SG_GetStatusBits
SG_GetStatusBits.restype = c_ulong
SG_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = SG_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_HasLastMsgTimerOverrun = lib.SG_HasLastMsgTimerOverrun
SG_HasLastMsgTimerOverrun.restype = c_bool
SG_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by SG_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = SG_HasLastMsgTimerOverrun(serial_number)

    return output


SG_Identify = lib.SG_Identify
SG_Identify.restype = c_void_p
SG_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = SG_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_LoadNamedSettings = lib.SG_LoadNamedSettings
SG_LoadNamedSettings.restype = c_bool
SG_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = SG_LoadNamedSettings(serial_number, settingsName)

    return output


SG_LoadSettings = lib.SG_LoadSettings
SG_LoadSettings.restype = c_bool
SG_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = SG_LoadSettings(serial_number)

    return output


SG_MessageQueueSize = lib.SG_MessageQueueSize
SG_MessageQueueSize.restype = c_int
SG_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = SG_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_Open = lib.SG_Open
SG_Open.restype = c_short
SG_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = SG_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_PersistSettings = lib.SG_PersistSettings
SG_PersistSettings.restype = c_bool
SG_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = SG_PersistSettings(serial_number)

    return output


SG_PollingDuration = lib.SG_PollingDuration
SG_PollingDuration.restype = c_long
SG_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = SG_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RegisterMessageCallback = lib.SG_RegisterMessageCallback
SG_RegisterMessageCallback.restype = c_void_p
SG_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = SG_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


SG_RequestDisplayMode = lib.SG_RequestDisplayMode
SG_RequestDisplayMode.restype = c_short
SG_RequestDisplayMode.argtypes = [POINTER(c_char)]


def request_display_mode(serial_number):
    # Requests the Display Mode.

    serial_number = POINTER(c_char)

    output = SG_RequestDisplayMode(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestForceCalib = lib.SG_RequestForceCalib
SG_RequestForceCalib.restype = c_short
SG_RequestForceCalib.argtypes = [POINTER(c_char)]


def request_force_calib(serial_number):
    # Requests the Force Calib.

    serial_number = POINTER(c_char)

    output = SG_RequestForceCalib(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestHubAnalogOutput = lib.SG_RequestHubAnalogOutput
SG_RequestHubAnalogOutput.restype = c_short
SG_RequestHubAnalogOutput.argtypes = [POINTER(c_char)]


def request_hub_analog_output(serial_number):
    # Requests the Hub Analog Output.

    serial_number = POINTER(c_char)

    output = SG_RequestHubAnalogOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestIOsettings = lib.SG_RequestIOsettings
SG_RequestIOsettings.restype = c_short
SG_RequestIOsettings.argtypes = [POINTER(c_char)]


def request_i_osettings(serial_number):
    # Requests the IO settings.

    serial_number = POINTER(c_char)

    output = SG_RequestIOsettings(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestLEDBrightness = lib.SG_RequestLEDBrightness
SG_RequestLEDBrightness.restype = c_short
SG_RequestLEDBrightness.argtypes = [POINTER(c_char)]


def request_l_e_d_brightness(serial_number):
    # Requests the LED brightness.

    serial_number = POINTER(c_char)

    output = SG_RequestLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestMaximumTravel = lib.SG_RequestMaximumTravel
SG_RequestMaximumTravel.restype = c_short
SG_RequestMaximumTravel.argtypes = [POINTER(c_char)]


def request_maximum_travel(serial_number):
    # Requests the maximum position.

    serial_number = POINTER(c_char)

    output = SG_RequestMaximumTravel(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestReading = lib.SG_RequestReading
SG_RequestReading.restype = c_short
SG_RequestReading.argtypes = [POINTER(c_char)]


def request_reading(serial_number):
    # Requests the current reading.

    serial_number = POINTER(c_char)

    output = SG_RequestReading(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestSettings = lib.SG_RequestSettings
SG_RequestSettings.restype = c_short
SG_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = SG_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_RequestStatus = lib.SG_RequestStatus
SG_RequestStatus.restype = c_short
SG_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status and reading from the device.

    serial_number = POINTER(c_char)

    output = SG_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_SetDisplayMode = lib.SG_SetDisplayMode
SG_SetDisplayMode.restype = c_short
SG_SetDisplayMode.argtypes = [POINTER(c_char), TSG_Display_Modes]


def set_display_mode(serial_number):
    # Sets the display mode.

    serial_number = POINTER(c_char)
    mode = TSG_Display_Modes()

    output = SG_SetDisplayMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


SG_SetForceCalib = lib.SG_SetForceCalib
SG_SetForceCalib.restype = c_short
SG_SetForceCalib.argtypes = [POINTER(c_char), c_uint]


def set_force_calib(serial_number):
    # Sets the maximum force in calibration.

    serial_number = POINTER(c_char)
    forceCalibration = c_uint()

    output = SG_SetForceCalib(serial_number, forceCalibration)
    if output != 0:
        raise KinesisException(output)


SG_SetHubAnalogOutput = lib.SG_SetHubAnalogOutput
SG_SetHubAnalogOutput.restype = c_short
SG_SetHubAnalogOutput.argtypes = [POINTER(c_char), TSG_Hub_Analogue_Modes]


def set_hub_analog_output(serial_number):
    # Sets the Hub Analog Output.

    serial_number = POINTER(c_char)
    hubAnalogOutput = TSG_Hub_Analogue_Modes()

    output = SG_SetHubAnalogOutput(serial_number, hubAnalogOutput)
    if output != 0:
        raise KinesisException(output)


SG_SetIOsettings = lib.SG_SetIOsettings
SG_SetIOsettings.restype = c_short
SG_SetIOsettings.argtypes = [POINTER(c_char), TSG_Hub_Analogue_Modes, TSG_Display_Modes, c_uint]


def set_i_osettings(serial_number):
    # Sets the input/output options.

    serial_number = POINTER(c_char)
    hubAnalogOutput = TSG_Hub_Analogue_Modes()
    displayMode = TSG_Display_Modes()
    calibrationForce = c_uint()

    output = SG_SetIOsettings(serial_number, hubAnalogOutput, displayMode, calibrationForce)
    if output != 0:
        raise KinesisException(output)


SG_SetIOsettingsBlock = lib.SG_SetIOsettingsBlock
SG_SetIOsettingsBlock.restype = c_short
SG_SetIOsettingsBlock.argtypes = [POINTER(c_char), TSG_IOSettings]


def set_i_osettings_block(serial_number):
    # Sets the input/output options in a block.

    serial_number = POINTER(c_char)
    inputOutputSettings = TSG_IOSettings()

    output = SG_SetIOsettingsBlock(serial_number, inputOutputSettings)
    if output != 0:
        raise KinesisException(output)


SG_SetLEDBrightness = lib.SG_SetLEDBrightness
SG_SetLEDBrightness.restype = c_short
SG_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = SG_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


SG_SetZero = lib.SG_SetZero
SG_SetZero.restype = c_short
SG_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    # Sets the voltage output to zero and defines the ensuing actuator position az zero.

    serial_number = POINTER(c_char)

    output = SG_SetZero(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_StartPolling = lib.SG_StartPolling
SG_StartPolling.restype = c_bool
SG_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = SG_StartPolling(serial_number, milliseconds)

    return output


SG_StopPolling = lib.SG_StopPolling
SG_StopPolling.restype = c_void_p
SG_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = SG_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


SG_TimeSinceLastMsgReceived = lib.SG_TimeSinceLastMsgReceived
SG_TimeSinceLastMsgReceived.restype = c_bool
SG_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = SG_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


SG_WaitForMessage = lib.SG_WaitForMessage
SG_WaitForMessage.restype = c_bool
SG_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = SG_WaitForMessage(serial_number, messageType, messageID, messageData)

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
