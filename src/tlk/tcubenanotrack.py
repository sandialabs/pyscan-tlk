from ctypes import (POINTER, c_bool, c_char, c_float, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KNA_FeedbackSource,
    KNA_HighOutputVoltageRoute,
    KNA_HighVoltageRange,
    KNA_TIARange,
    NT_FeedbackSource,
    NT_Mode,
    NT_OddOrEven,
    NT_OutputVoltageRoute,
    NT_SignalState,
    NT_TIARange,
    NT_TIARangeMode,
    NT_VoltageRange)
from .definitions.structures import (
    BNT_IO_Settings,
    KNA_IOSettings,
    KNA_TIARangeParameters,
    KNA_TIAReading,
    NT_CircleDiameterLUT,
    NT_CircleParameters,
    NT_HVComponent,
    NT_IOSettings,
    NT_LowPassFilterParameters,
    NT_TIARangeParameters,
    NT_TIAReading,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.NanoTrak.DLL")

NT_CheckConnection = lib.NT_CheckConnection
NT_CheckConnection.restype = c_bool
NT_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = NT_CheckConnection(serial_number)

    return output


NT_ClearMessageQueue = lib.NT_ClearMessageQueue
NT_ClearMessageQueue.restype = c_void_p
NT_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # clears the message queue.

    serial_number = POINTER(c_char)

    output = NT_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_Close = lib.NT_Close
NT_Close.restype = c_void_p
NT_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = NT_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_Disconnect = lib.NT_Disconnect
NT_Disconnect.restype = c_short
NT_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = NT_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_EnableLastMsgTimer = lib.NT_EnableLastMsgTimer
NT_EnableLastMsgTimer.restype = c_void_p
NT_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = NT_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


NT_GetCircleDiameter = lib.NT_GetCircleDiameter
NT_GetCircleDiameter.restype = c_long
NT_GetCircleDiameter.argtypes = [POINTER(c_char)]


def get_circle_diameter(serial_number):
    # Gets the scan circle diameter.

    serial_number = POINTER(c_char)

    output = NT_GetCircleDiameter(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetCircleDiameterLUT = lib.NT_GetCircleDiameterLUT
NT_GetCircleDiameterLUT.restype = c_short
NT_GetCircleDiameterLUT.argtypes = [POINTER(c_char), NT_CircleDiameterLUT]


def get_circle_diameter_l_u_t(serial_number):
    # Gets the scan circle diameter Lookup Table (LUT).

    serial_number = POINTER(c_char)
    LUT = NT_CircleDiameterLUT()

    output = NT_GetCircleDiameterLUT(serial_number, LUT)
    if output != 0:
        raise KinesisException(output)


NT_GetCircleHomePosition = lib.NT_GetCircleHomePosition
NT_GetCircleHomePosition.restype = c_short
NT_GetCircleHomePosition.argtypes = [POINTER(c_char), NT_HVComponent]


def get_circle_home_position(serial_number):
    # Gets the home position of the scan circle.

    serial_number = POINTER(c_char)
    position = NT_HVComponent()

    output = NT_GetCircleHomePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


NT_GetCircleParams = lib.NT_GetCircleParams
NT_GetCircleParams.restype = c_short
NT_GetCircleParams.argtypes = [POINTER(c_char), NT_CircleParameters]


def get_circle_params(serial_number):
    # Gets the scanning circle parameters.

    serial_number = POINTER(c_char)
    params = NT_CircleParameters()

    output = NT_GetCircleParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


NT_GetCirclePosition = lib.NT_GetCirclePosition
NT_GetCirclePosition.restype = c_short
NT_GetCirclePosition.argtypes = [POINTER(c_char), NT_HVComponent]


def get_circle_position(serial_number):
    # Gets the current scan circle centre position.

    serial_number = POINTER(c_char)
    position = NT_HVComponent()

    output = NT_GetCirclePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


NT_GetFeedbackSource = lib.NT_GetFeedbackSource
NT_GetFeedbackSource.restype = NT_FeedbackSource
NT_GetFeedbackSource.argtypes = [POINTER(c_char)]


def get_feedback_source(serial_number):
    # Gets the NanoTrak feedback source.

    serial_number = POINTER(c_char)

    output = NT_GetFeedbackSource(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetFirmwareVersion = lib.NT_GetFirmwareVersion
NT_GetFirmwareVersion.restype = c_ulong
NT_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = NT_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetGain = lib.NT_GetGain
NT_GetGain.restype = c_short
NT_GetGain.argtypes = [POINTER(c_char)]


def get_gain(serial_number):
    # Gets the control loop gain.

    serial_number = POINTER(c_char)

    output = NT_GetGain(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetHardwareInfo = lib.NT_GetHardwareInfo
NT_GetHardwareInfo.restype = c_short
NT_GetHardwareInfo.argtypes = [
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

    output = NT_GetHardwareInfo(
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


NT_GetHardwareInfoBlock = lib.NT_GetHardwareInfoBlock
NT_GetHardwareInfoBlock.restype = c_short
NT_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = NT_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


NT_GetHubBay = lib.NT_GetHubBay
NT_GetHubBay.restype = POINTER(c_char)
NT_GetHubBay.argtypes = [POINTER(c_char)]


def get_hub_bay(serial_number):
    # Gets the hub bay number this device is fitted to.

    serial_number = POINTER(c_char)

    output = NT_GetHubBay(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetIOsettings = lib.NT_GetIOsettings
NT_GetIOsettings.restype = c_short
NT_GetIOsettings.argtypes = [
    POINTER(c_char),
    KNA_HighVoltageRange,
    NT_VoltageRange,
    KNA_HighOutputVoltageRoute,
    NT_OutputVoltageRoute]


def get_i_osettings(serial_number):
    # Gets the input/output options.

    serial_number = POINTER(c_char)
    highVoltageOutRange = KNA_HighVoltageRange()
    lowVoltageOutRange = NT_VoltageRange()
    highVoltageOutputRoute = KNA_HighOutputVoltageRoute()
    lowVoltageOutputRoute = NT_OutputVoltageRoute()

    output = NT_GetIOsettings(
        serial_number,
        highVoltageOutRange,
        lowVoltageOutRange,
        highVoltageOutputRoute,
        lowVoltageOutputRoute)
    if output != 0:
        raise KinesisException(output)


NT_GetIOsettingsBlock = lib.NT_GetIOsettingsBlock
NT_GetIOsettingsBlock.restype = c_short
NT_GetIOsettingsBlock.argtypes = [POINTER(c_char), BNT_IO_Settings, KNA_IOSettings, NT_IOSettings, c_long]


def get_i_osettings_block(serial_number, channel):
    # Gets the input/output settings in a block.

    serial_number = POINTER(c_char)
    IOsettings = BNT_IO_Settings()
    IOsettings = KNA_IOSettings()
    IOsettings = NT_IOSettings()
    channel = c_long()

    output = NT_GetIOsettingsBlock(serial_number, IOsettings, IOsettings, IOsettings, channel)
    if output != 0:
        raise KinesisException(output)


NT_GetLEDBrightness = lib.NT_GetLEDBrightness
NT_GetLEDBrightness.restype = c_short
NT_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = NT_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetMode = lib.NT_GetMode
NT_GetMode.restype = NT_Mode
NT_GetMode.argtypes = [POINTER(c_char)]


def get_mode(serial_number):
    # Gets the nanoTrak operating mode.

    serial_number = POINTER(c_char)

    output = NT_GetMode(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetNextMessage = lib.NT_GetNextMessage
NT_GetNextMessage.restype = c_bool
NT_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = NT_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


NT_GetPhaseCompensationParams = lib.NT_GetPhaseCompensationParams
NT_GetPhaseCompensationParams.restype = c_short
NT_GetPhaseCompensationParams.argtypes = [POINTER(c_char), NT_HVComponent]


def get_phase_compensation_params(serial_number):
    # Gets the phase compensation parameters.

    serial_number = POINTER(c_char)
    params = NT_HVComponent()

    output = NT_GetPhaseCompensationParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


NT_GetRangeMode = lib.NT_GetRangeMode
NT_GetRangeMode.restype = c_short
NT_GetRangeMode.argtypes = [POINTER(c_char), NT_TIARangeMode, NT_OddOrEven]


def get_range_mode(serial_number):
    # Get the TIA Range Mode and OddEven mode.

    serial_number = POINTER(c_char)
    mode = NT_TIARangeMode()
    oddOrEven = NT_OddOrEven()

    output = NT_GetRangeMode(serial_number, mode, oddOrEven)
    if output != 0:
        raise KinesisException(output)


NT_GetReading = lib.NT_GetReading
NT_GetReading.restype = c_short
NT_GetReading.argtypes = [POINTER(c_char), NT_TIAReading, KNA_TIAReading]


def get_reading(serial_number):
    # Gets a reading.

    serial_number = POINTER(c_char)
    reading = NT_TIAReading()
    reading = KNA_TIAReading()

    output = NT_GetReading(serial_number, reading, reading)
    if output != 0:
        raise KinesisException(output)


NT_GetSignalState = lib.NT_GetSignalState
NT_GetSignalState.restype = NT_SignalState
NT_GetSignalState.argtypes = [POINTER(c_char)]


def get_signal_state(serial_number):
    # Gets the NanoTrak signal state.

    serial_number = POINTER(c_char)

    output = NT_GetSignalState(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetSoftwareVersion = lib.NT_GetSoftwareVersion
NT_GetSoftwareVersion.restype = c_ulong
NT_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = NT_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetStatusBits = lib.NT_GetStatusBits
NT_GetStatusBits.restype = c_ulong
NT_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = NT_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetTIALPFilterParams = lib.NT_GetTIALPFilterParams
NT_GetTIALPFilterParams.restype = c_short
NT_GetTIALPFilterParams.argtypes = [POINTER(c_char), NT_LowPassFilterParameters]


def get_t_i_a_l_p_filter_params(serial_number):
    # Gets the TIA long pass filter parameters.

    serial_number = POINTER(c_char)
    params = NT_LowPassFilterParameters()

    output = NT_GetTIALPFilterParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


NT_GetTIARange = lib.NT_GetTIARange
NT_GetTIARange.restype = NT_TIARange
NT_GetTIARange.argtypes = [POINTER(c_char)]


def get_t_i_a_range(serial_number):
    # Gets the TIA range.

    serial_number = POINTER(c_char)

    output = NT_GetTIARange(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_GetTIArangeParams = lib.NT_GetTIArangeParams
NT_GetTIArangeParams.restype = c_short
NT_GetTIArangeParams.argtypes = [POINTER(c_char), NT_TIARangeParameters, KNA_TIARangeParameters]


def get_t_i_arange_params(serial_number):
    # Gets the TIA range parameters.

    serial_number = POINTER(c_char)
    params = NT_TIARangeParameters()
    params = KNA_TIARangeParameters()

    output = NT_GetTIArangeParams(serial_number, params, params)
    if output != 0:
        raise KinesisException(output)


NT_GetTrackingThresholdSignal = lib.NT_GetTrackingThresholdSignal
NT_GetTrackingThresholdSignal.restype = c_float
NT_GetTrackingThresholdSignal.argtypes = [POINTER(c_char)]


def get_tracking_threshold_signal(serial_number):
    # Gets the tracking threshold signal.

    serial_number = POINTER(c_char)

    output = NT_GetTrackingThresholdSignal(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_HasLastMsgTimerOverrun = lib.NT_HasLastMsgTimerOverrun
NT_HasLastMsgTimerOverrun.restype = c_bool
NT_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by NT_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = NT_HasLastMsgTimerOverrun(serial_number)

    return output


NT_HomeCircle = lib.NT_HomeCircle
NT_HomeCircle.restype = c_short
NT_HomeCircle.argtypes = [POINTER(c_char)]


def home_circle(serial_number):
    # Move the scan circle to the home position.

    serial_number = POINTER(c_char)

    output = NT_HomeCircle(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_Identify = lib.NT_Identify
NT_Identify.restype = c_void_p
NT_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = NT_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_LoadNamedSettings = lib.NT_LoadNamedSettings
NT_LoadNamedSettings.restype = c_bool
NT_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = NT_LoadNamedSettings(serial_number, settingsName)

    return output


NT_LoadSettings = lib.NT_LoadSettings
NT_LoadSettings.restype = c_bool
NT_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = NT_LoadSettings(serial_number)

    return output


NT_MessageQueueSize = lib.NT_MessageQueueSize
NT_MessageQueueSize.restype = c_int
NT_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = NT_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_Open = lib.NT_Open
NT_Open.restype = c_short
NT_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = NT_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_PersistSettings = lib.NT_PersistSettings
NT_PersistSettings.restype = c_bool
NT_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = NT_PersistSettings(serial_number)

    return output


NT_PollingDuration = lib.NT_PollingDuration
NT_PollingDuration.restype = c_long
NT_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = NT_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RegisterMessageCallback = lib.NT_RegisterMessageCallback
NT_RegisterMessageCallback.restype = c_void_p
NT_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = NT_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


NT_RequestCircleDiameterLUT = lib.NT_RequestCircleDiameterLUT
NT_RequestCircleDiameterLUT.restype = c_short
NT_RequestCircleDiameterLUT.argtypes = [POINTER(c_char)]


def request_circle_diameter_l_u_t(serial_number):
    # Requests the scan circle diameter Lookup Table (LUT).

    serial_number = POINTER(c_char)

    output = NT_RequestCircleDiameterLUT(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestCircleHomePosition = lib.NT_RequestCircleHomePosition
NT_RequestCircleHomePosition.restype = c_short
NT_RequestCircleHomePosition.argtypes = [POINTER(c_char)]


def request_circle_home_position(serial_number):
    # Requests the home position of the scan circle.

    serial_number = POINTER(c_char)

    output = NT_RequestCircleHomePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestCircleParams = lib.NT_RequestCircleParams
NT_RequestCircleParams.restype = c_short
NT_RequestCircleParams.argtypes = [POINTER(c_char)]


def request_circle_params(serial_number):
    # Requests the scanning circle parameters.

    serial_number = POINTER(c_char)

    output = NT_RequestCircleParams(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestCirclePosition = lib.NT_RequestCirclePosition
NT_RequestCirclePosition.restype = c_short
NT_RequestCirclePosition.argtypes = [POINTER(c_char)]


def request_circle_position(serial_number):
    # Requests the current scan circle centre position.

    serial_number = POINTER(c_char)

    output = NT_RequestCirclePosition(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestFeedbackSource = lib.NT_RequestFeedbackSource
NT_RequestFeedbackSource.restype = c_short
NT_RequestFeedbackSource.argtypes = [POINTER(c_char)]


def request_feedback_source(serial_number):
    # Requests the NanoTrak Feedback Source.

    serial_number = POINTER(c_char)

    output = NT_RequestFeedbackSource(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestGain = lib.NT_RequestGain
NT_RequestGain.restype = c_short
NT_RequestGain.argtypes = [POINTER(c_char)]


def request_gain(serial_number):
    # Requests the control loop gain.

    serial_number = POINTER(c_char)

    output = NT_RequestGain(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestIOsettings = lib.NT_RequestIOsettings
NT_RequestIOsettings.restype = c_short
NT_RequestIOsettings.argtypes = [POINTER(c_char)]


def request_i_osettings(serial_number):
    # Requests the input/output options.

    serial_number = POINTER(c_char)

    output = NT_RequestIOsettings(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestMode = lib.NT_RequestMode
NT_RequestMode.restype = c_short
NT_RequestMode.argtypes = [POINTER(c_char)]


def request_mode(serial_number):
    # Requests the NanoTrak mode.

    serial_number = POINTER(c_char)

    output = NT_RequestMode(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestPhaseCompensationParams = lib.NT_RequestPhaseCompensationParams
NT_RequestPhaseCompensationParams.restype = c_short
NT_RequestPhaseCompensationParams.argtypes = [POINTER(c_char)]


def request_phase_compensation_params(serial_number):
    # Requests the phase compensation parameters.

    serial_number = POINTER(c_char)

    output = NT_RequestPhaseCompensationParams(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestReading = lib.NT_RequestReading
NT_RequestReading.restype = c_short
NT_RequestReading.argtypes = [POINTER(c_char)]


def request_reading(serial_number):
    # Requests a TIA reading.

    serial_number = POINTER(c_char)

    output = NT_RequestReading(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestSettings = lib.NT_RequestSettings
NT_RequestSettings.restype = c_short
NT_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = NT_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestSignalState = lib.NT_RequestSignalState
NT_RequestSignalState.restype = c_short
NT_RequestSignalState.argtypes = [POINTER(c_char)]


def request_signal_state(serial_number):
    # Requests the NanoTrak signal state.

    serial_number = POINTER(c_char)

    output = NT_RequestSignalState(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestStatus = lib.NT_RequestStatus
NT_RequestStatus.restype = c_short
NT_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status bits and reading.

    serial_number = POINTER(c_char)

    output = NT_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestStatusBits = lib.NT_RequestStatusBits
NT_RequestStatusBits.restype = c_short
NT_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = NT_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestTIALPFilterParams = lib.NT_RequestTIALPFilterParams
NT_RequestTIALPFilterParams.restype = c_short
NT_RequestTIALPFilterParams.argtypes = [POINTER(c_char)]


def request_t_i_a_l_p_filter_params(serial_number):
    # Requests the NanoTrak tracking threshold signal.

    serial_number = POINTER(c_char)

    output = NT_RequestTIALPFilterParams(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestTIArangeParams = lib.NT_RequestTIArangeParams
NT_RequestTIArangeParams.restype = c_short
NT_RequestTIArangeParams.argtypes = [POINTER(c_char)]


def request_t_i_arange_params(serial_number):
    # Requests the TIA range parameters.

    serial_number = POINTER(c_char)

    output = NT_RequestTIArangeParams(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_RequestTrackingThresholdSignal = lib.NT_RequestTrackingThresholdSignal
NT_RequestTrackingThresholdSignal.restype = c_short
NT_RequestTrackingThresholdSignal.argtypes = [POINTER(c_char)]


def request_tracking_threshold_signal(serial_number):
    # Requests the NanoTrak tracking threshold signal.

    serial_number = POINTER(c_char)

    output = NT_RequestTrackingThresholdSignal(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_SetCircleDiameter = lib.NT_SetCircleDiameter
NT_SetCircleDiameter.restype = c_short
NT_SetCircleDiameter.argtypes = [POINTER(c_char), c_long]


def set_circle_diameter(serial_number):
    # Sets the scan circle diameter.

    serial_number = POINTER(c_char)
    diameter = c_long()

    output = NT_SetCircleDiameter(serial_number, diameter)
    if output != 0:
        raise KinesisException(output)


NT_SetCircleDiameterLUT = lib.NT_SetCircleDiameterLUT
NT_SetCircleDiameterLUT.restype = c_short
NT_SetCircleDiameterLUT.argtypes = [POINTER(c_char), NT_CircleDiameterLUT]


def set_circle_diameter_l_u_t(serial_number):
    # Sets the scan circle diameter Lookup Table (LUT).

    serial_number = POINTER(c_char)
    LUT = NT_CircleDiameterLUT()

    output = NT_SetCircleDiameterLUT(serial_number, LUT)
    if output != 0:
        raise KinesisException(output)


NT_SetCircleHomePosition = lib.NT_SetCircleHomePosition
NT_SetCircleHomePosition.restype = c_short
NT_SetCircleHomePosition.argtypes = [POINTER(c_char), NT_HVComponent]


def set_circle_home_position(serial_number):
    # Sets the home position of the scan circle.

    serial_number = POINTER(c_char)
    position = NT_HVComponent()

    output = NT_SetCircleHomePosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


NT_SetCircleParams = lib.NT_SetCircleParams
NT_SetCircleParams.restype = c_short
NT_SetCircleParams.argtypes = [POINTER(c_char), NT_CircleParameters]


def set_circle_params(serial_number):
    # Sets the scanning circle parameters.

    serial_number = POINTER(c_char)
    params = NT_CircleParameters()

    output = NT_SetCircleParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


NT_SetFeedbackSource = lib.NT_SetFeedbackSource
NT_SetFeedbackSource.restype = c_short
NT_SetFeedbackSource.argtypes = [POINTER(c_char), NT_FeedbackSource, KNA_FeedbackSource]


def set_feedback_source(serial_number):
    # Sets the NanoTrak feedback source.

    serial_number = POINTER(c_char)
    input = NT_FeedbackSource()
    input = KNA_FeedbackSource()

    output = NT_SetFeedbackSource(serial_number, input, input)
    if output != 0:
        raise KinesisException(output)


NT_SetGain = lib.NT_SetGain
NT_SetGain.restype = c_short
NT_SetGain.argtypes = [POINTER(c_char), c_short]


def set_gain(serial_number):
    # Sets the control loop gain.

    serial_number = POINTER(c_char)
    gain = c_short()

    output = NT_SetGain(serial_number, gain)
    if output != 0:
        raise KinesisException(output)


NT_SetIOsettings = lib.NT_SetIOsettings
NT_SetIOsettings.restype = c_short
NT_SetIOsettings.argtypes = [
    POINTER(c_char),
    KNA_HighVoltageRange,
    NT_VoltageRange,
    KNA_HighOutputVoltageRoute,
    NT_OutputVoltageRoute]


def set_i_osettings(serial_number):
    # Sets the input/output options.

    serial_number = POINTER(c_char)
    highVoltageOutRange = KNA_HighVoltageRange()
    lowVoltageOutRange = NT_VoltageRange()
    highVoltageOutputRoute = KNA_HighOutputVoltageRoute()
    lowVoltageOutputRoute = NT_OutputVoltageRoute()

    output = NT_SetIOsettings(
        serial_number,
        highVoltageOutRange,
        lowVoltageOutRange,
        highVoltageOutputRoute,
        lowVoltageOutputRoute)
    if output != 0:
        raise KinesisException(output)


NT_SetIOsettingsBlock = lib.NT_SetIOsettingsBlock
NT_SetIOsettingsBlock.restype = c_short
NT_SetIOsettingsBlock.argtypes = [POINTER(c_char), BNT_IO_Settings, KNA_IOSettings, NT_IOSettings, c_long]


def set_i_osettings_block(serial_number, channel):
    # Sets the input/output options in a block.

    serial_number = POINTER(c_char)
    IOsettings = BNT_IO_Settings()
    IOsettings = KNA_IOSettings()
    IOsettings = NT_IOSettings()
    channel = c_long()

    output = NT_SetIOsettingsBlock(serial_number, IOsettings, IOsettings, IOsettings, channel)
    if output != 0:
        raise KinesisException(output)


NT_SetLEDBrightness = lib.NT_SetLEDBrightness
NT_SetLEDBrightness.restype = c_short
NT_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = NT_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


NT_SetMode = lib.NT_SetMode
NT_SetMode.restype = c_short
NT_SetMode.argtypes = [POINTER(c_char), NT_Mode]


def set_mode(serial_number):
    # Setsthe nanoTrak operating mode.

    serial_number = POINTER(c_char)
    mode = NT_Mode()

    output = NT_SetMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


NT_SetPhaseCompensationParams = lib.NT_SetPhaseCompensationParams
NT_SetPhaseCompensationParams.restype = c_short
NT_SetPhaseCompensationParams.argtypes = [POINTER(c_char), NT_HVComponent]


def set_phase_compensation_params(serial_number):
    # Sets the phase compensation parameters.

    serial_number = POINTER(c_char)
    params = NT_HVComponent()

    output = NT_SetPhaseCompensationParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


NT_SetRangeMode = lib.NT_SetRangeMode
NT_SetRangeMode.restype = c_short
NT_SetRangeMode.argtypes = [POINTER(c_char), NT_TIARangeMode, NT_OddOrEven]


def set_range_mode(serial_number):
    # Get the TIA Range Mode and OddEven mode.

    serial_number = POINTER(c_char)
    mode = NT_TIARangeMode()
    oddOrEven = NT_OddOrEven()

    output = NT_SetRangeMode(serial_number, mode, oddOrEven)
    if output != 0:
        raise KinesisException(output)


NT_SetTIALPFilterParams = lib.NT_SetTIALPFilterParams
NT_SetTIALPFilterParams.restype = c_short
NT_SetTIALPFilterParams.argtypes = [POINTER(c_char), NT_LowPassFilterParameters]


def set_t_i_a_l_p_filter_params(serial_number):
    # Sets the TIA long pass filter parameters.

    serial_number = POINTER(c_char)
    params = NT_LowPassFilterParameters()

    output = NT_SetTIALPFilterParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


NT_SetTIARange = lib.NT_SetTIARange
NT_SetTIARange.restype = c_short
NT_SetTIARange.argtypes = [POINTER(c_char), NT_TIARange, KNA_TIARange]


def set_t_i_a_range(serial_number):
    # Sets TIA range.

    serial_number = POINTER(c_char)
    range = NT_TIARange()
    range = KNA_TIARange()

    output = NT_SetTIARange(serial_number, range, range)
    if output != 0:
        raise KinesisException(output)


NT_SetTIArangeParams = lib.NT_SetTIArangeParams
NT_SetTIArangeParams.restype = c_short
NT_SetTIArangeParams.argtypes = [POINTER(c_char), NT_TIARangeParameters, KNA_TIARangeParameters]


def set_t_i_arange_params(serial_number):
    # Sets the TIA range parameters.

    serial_number = POINTER(c_char)
    params = NT_TIARangeParameters()
    params = KNA_TIARangeParameters()

    output = NT_SetTIArangeParams(serial_number, params, params)
    if output != 0:
        raise KinesisException(output)


NT_SetTrackingThresholdSignal = lib.NT_SetTrackingThresholdSignal
NT_SetTrackingThresholdSignal.restype = c_short
NT_SetTrackingThresholdSignal.argtypes = [POINTER(c_char), c_float]


def set_tracking_threshold_signal(serial_number):
    # Sets the tracking threshold signal.

    serial_number = POINTER(c_char)
    threshold = c_float()

    output = NT_SetTrackingThresholdSignal(serial_number, threshold)
    if output != 0:
        raise KinesisException(output)


NT_StartPolling = lib.NT_StartPolling
NT_StartPolling.restype = c_bool
NT_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = NT_StartPolling(serial_number, milliseconds)

    return output


NT_StopPolling = lib.NT_StopPolling
NT_StopPolling.restype = c_void_p
NT_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = NT_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


NT_TimeSinceLastMsgReceived = lib.NT_TimeSinceLastMsgReceived
NT_TimeSinceLastMsgReceived.restype = c_bool
NT_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = NT_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


NT_WaitForMessage = lib.NT_WaitForMessage
NT_WaitForMessage.restype = c_bool
NT_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = NT_WaitForMessage(serial_number, messageType, messageID, messageData)

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
