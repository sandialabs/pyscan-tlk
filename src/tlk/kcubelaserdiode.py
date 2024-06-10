from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_float,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KLD_RAMPUP,
    KLD_TrigPolarity,
    KLD_TriggerMode,
    KLS_TrigPolarity,
    KLS_TriggerMode,
    LD_DisplayUnits,
    LD_InputSourceFlags,
    LD_POLARITY)
from .definitions.structures import (
    KLD_MMIParams,
    KLD_TrigIOParams,
    KLS_MMIParams,
    KLS_TrigIOParams,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.LaserDiode.dll")

LD_CanDeviceLockFrontPanel = lib.LD_CanDeviceLockFrontPanel
LD_CanDeviceLockFrontPanel.restype = c_bool
LD_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = LD_CanDeviceLockFrontPanel(serial_number)

    return output


LD_CheckConnection = lib.LD_CheckConnection
LD_CheckConnection.restype = c_bool
LD_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = LD_CheckConnection(serial_number)

    return output


LD_ClearMessageQueue = lib.LD_ClearMessageQueue
LD_ClearMessageQueue.restype = c_void_p
LD_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = LD_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_Close = lib.LD_Close
LD_Close.restype = c_void_p
LD_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = LD_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_Disable = lib.LD_Disable
LD_Disable.restype = c_short
LD_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable laser.

    serial_number = POINTER(c_char)

    output = LD_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_DisableOutput = lib.LD_DisableOutput
LD_DisableOutput.restype = c_short
LD_DisableOutput.argtypes = [POINTER(c_char)]


def disable_output(serial_number):
    # Switch laser off.

    serial_number = POINTER(c_char)

    output = LD_DisableOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_Enable = lib.LD_Enable
LD_Enable.restype = c_short
LD_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable laser for computer control.

    serial_number = POINTER(c_char)

    output = LD_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_EnableLastMsgTimer = lib.LD_EnableLastMsgTimer
LD_EnableLastMsgTimer.restype = c_void_p
LD_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = LD_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


LD_EnableMaxCurrentAdjust = lib.LD_EnableMaxCurrentAdjust
LD_EnableMaxCurrentAdjust.restype = c_short
LD_EnableMaxCurrentAdjust.argtypes = [POINTER(c_char), c_bool, c_bool]


def enable_max_current_adjust(serial_number):
    # Enables the maximum current adjust mode.

    serial_number = POINTER(c_char)
    enableAdjust = c_bool()
    enableDiode = c_bool()

    output = LD_EnableMaxCurrentAdjust(serial_number, enableAdjust, enableDiode)
    if output != 0:
        raise KinesisException(output)


LD_EnableOutput = lib.LD_EnableOutput
LD_EnableOutput.restype = c_short
LD_EnableOutput.argtypes = [POINTER(c_char)]


def enable_output(serial_number):
    # Switch laser on.

    serial_number = POINTER(c_char)

    output = LD_EnableOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_EnableTIAGainAdjust = lib.LD_EnableTIAGainAdjust
LD_EnableTIAGainAdjust.restype = c_short
LD_EnableTIAGainAdjust.argtypes = [POINTER(c_char), c_bool]


def enable_t_i_a_gain_adjust(serial_number):
    # Enables the tia gain adjustment mode.

    serial_number = POINTER(c_char)
    enable = c_bool()

    output = LD_EnableTIAGainAdjust(serial_number, enable)
    if output != 0:
        raise KinesisException(output)


LD_FindTIAGain = lib.LD_FindTIAGain
LD_FindTIAGain.restype = c_short
LD_FindTIAGain.argtypes = [POINTER(c_char)]


def find_t_i_a_gain(serial_number):
    # Performs the FindTIAGain calibration.

    serial_number = POINTER(c_char)

    output = LD_FindTIAGain(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetControlSource = lib.LD_GetControlSource
LD_GetControlSource.restype = LD_InputSourceFlags
LD_GetControlSource.argtypes = [POINTER(c_char)]


def get_control_source(serial_number):
    # Gets the control input source.

    serial_number = POINTER(c_char)

    output = LD_GetControlSource(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetDisplayUnits = lib.LD_GetDisplayUnits
LD_GetDisplayUnits.restype = LD_DisplayUnits
LD_GetDisplayUnits.argtypes = [POINTER(c_char)]


def get_display_units(serial_number):
    # Gets the hardware display units.

    serial_number = POINTER(c_char)

    output = LD_GetDisplayUnits(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetFirmwareVersion = lib.LD_GetFirmwareVersion
LD_GetFirmwareVersion.restype = c_ulong
LD_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = LD_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetFrontPanelLocked = lib.LD_GetFrontPanelLocked
LD_GetFrontPanelLocked.restype = c_bool
LD_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = LD_GetFrontPanelLocked(serial_number)

    return output


LD_GetHardwareInfo = lib.LD_GetHardwareInfo
LD_GetHardwareInfo.restype = c_short
LD_GetHardwareInfo.argtypes = [
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

    output = LD_GetHardwareInfo(
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


LD_GetHardwareInfoBlock = lib.LD_GetHardwareInfoBlock
LD_GetHardwareInfoBlock.restype = c_short
LD_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = LD_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


LD_GetInterlockState = lib.LD_GetInterlockState
LD_GetInterlockState.restype = c_byte
LD_GetInterlockState.argtypes = [POINTER(c_char)]


def get_interlock_state(serial_number):
    # Gets the Interlock State.

    serial_number = POINTER(c_char)

    output = LD_GetInterlockState(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetLEDBrightness = lib.LD_GetLEDBrightness
LD_GetLEDBrightness.restype = c_long
LD_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = LD_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetLaserDiodeCurrentReading = lib.LD_GetLaserDiodeCurrentReading
LD_GetLaserDiodeCurrentReading.restype = c_long
LD_GetLaserDiodeCurrentReading.argtypes = [POINTER(c_char)]


def get_laser_diode_current_reading(serial_number):
    # Gets current Current reading.

    serial_number = POINTER(c_char)

    output = LD_GetLaserDiodeCurrentReading(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetLaserPolarity = lib.LD_GetLaserPolarity
LD_GetLaserPolarity.restype = LD_POLARITY
LD_GetLaserPolarity.argtypes = [POINTER(c_char)]


def get_laser_polarity(serial_number):
    # Gets the laser polarity.

    serial_number = POINTER(c_char)

    output = LD_GetLaserPolarity(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetLaserSetPoint = lib.LD_GetLaserSetPoint
LD_GetLaserSetPoint.restype = c_long
LD_GetLaserSetPoint.argtypes = [POINTER(c_char)]


def get_laser_set_point(serial_number):
    # Gets the Laser Diode Current currently set.

    serial_number = POINTER(c_char)

    output = LD_GetLaserSetPoint(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetMaxCurrentDigPot = lib.LD_GetMaxCurrentDigPot
LD_GetMaxCurrentDigPot.restype = c_long
LD_GetMaxCurrentDigPot.argtypes = [POINTER(c_char)]


def get_max_current_dig_pot(serial_number):
    # Gets the maximum current dig pot position.

    serial_number = POINTER(c_char)

    output = LD_GetMaxCurrentDigPot(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetNextMessage = lib.LD_GetNextMessage
LD_GetNextMessage.restype = c_bool
LD_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = LD_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


LD_GetPhotoCurrentReading = lib.LD_GetPhotoCurrentReading
LD_GetPhotoCurrentReading.restype = c_long
LD_GetPhotoCurrentReading.argtypes = [POINTER(c_char)]


def get_photo_current_reading(serial_number):
    # Gets current Photo Current reading.

    serial_number = POINTER(c_char)

    output = LD_GetPhotoCurrentReading(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetRampupMode = lib.LD_GetRampupMode
LD_GetRampupMode.restype = KLD_RAMPUP
LD_GetRampupMode.argtypes = [POINTER(c_char)]


def get_rampup_mode(serial_number):
    # Gets the ramp up mode.

    serial_number = POINTER(c_char)

    output = LD_GetRampupMode(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetSoftwareVersion = lib.LD_GetSoftwareVersion
LD_GetSoftwareVersion.restype = c_ulong
LD_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = LD_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetStatusBits = lib.LD_GetStatusBits
LD_GetStatusBits.restype = c_ulong
LD_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = LD_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetVoltageReading = lib.LD_GetVoltageReading
LD_GetVoltageReading.restype = c_long
LD_GetVoltageReading.argtypes = [POINTER(c_char)]


def get_voltage_reading(serial_number):
    # Gets current Voltage reading.

    serial_number = POINTER(c_char)

    output = LD_GetVoltageReading(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_GetWACalibFactor = lib.LD_GetWACalibFactor
LD_GetWACalibFactor.restype = c_float
LD_GetWACalibFactor.argtypes = [POINTER(c_char)]


def get_w_a_calib_factor(serial_number):
    # Gets the W/A calibration factor.

    serial_number = POINTER(c_char)

    output = LD_GetWACalibFactor(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_HasLastMsgTimerOverrun = lib.LD_HasLastMsgTimerOverrun
LD_HasLastMsgTimerOverrun.restype = c_bool
LD_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by LD_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = LD_HasLastMsgTimerOverrun(serial_number)

    return output


LD_Identify = lib.LD_Identify
LD_Identify.restype = c_void_p
LD_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = LD_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_LoadNamedSettings = lib.LD_LoadNamedSettings
LD_LoadNamedSettings.restype = c_bool
LD_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = LD_LoadNamedSettings(serial_number, settingsName)

    return output


LD_LoadSettings = lib.LD_LoadSettings
LD_LoadSettings.restype = c_bool
LD_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = LD_LoadSettings(serial_number)

    return output


LD_MessageQueueSize = lib.LD_MessageQueueSize
LD_MessageQueueSize.restype = c_int
LD_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = LD_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_Open = lib.LD_Open
LD_Open.restype = c_short
LD_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = LD_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_PersistSettings = lib.LD_PersistSettings
LD_PersistSettings.restype = c_bool
LD_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = LD_PersistSettings(serial_number)

    return output


LD_PollingDuration = lib.LD_PollingDuration
LD_PollingDuration.restype = c_long
LD_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = LD_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RegisterMessageCallback = lib.LD_RegisterMessageCallback
LD_RegisterMessageCallback.restype = c_void_p
LD_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = LD_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


LD_RequestControlSource = lib.LD_RequestControlSource
LD_RequestControlSource.restype = c_short
LD_RequestControlSource.argtypes = [POINTER(c_char)]


def request_control_source(serial_number):
    # Gets the control input source.

    serial_number = POINTER(c_char)

    output = LD_RequestControlSource(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestDisplay = lib.LD_RequestDisplay
LD_RequestDisplay.restype = c_short
LD_RequestDisplay.argtypes = [POINTER(c_char)]


def request_display(serial_number):
    # Requests the display parameters (Units and Intensity).

    serial_number = POINTER(c_char)

    output = LD_RequestDisplay(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestFrontPanelLocked = lib.LD_RequestFrontPanelLocked
LD_RequestFrontPanelLocked.restype = c_short
LD_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = LD_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestLaserPolarity = lib.LD_RequestLaserPolarity
LD_RequestLaserPolarity.restype = c_short
LD_RequestLaserPolarity.argtypes = [POINTER(c_char)]


def request_laser_polarity(serial_number):
    # Requests the laser polarity.

    serial_number = POINTER(c_char)

    output = LD_RequestLaserPolarity(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestLaserSetPoint = lib.LD_RequestLaserSetPoint
LD_RequestLaserSetPoint.restype = c_short
LD_RequestLaserSetPoint.argtypes = [POINTER(c_char)]


def request_laser_set_point(serial_number):
    # Sets the output point (power / current / voltage).

    serial_number = POINTER(c_char)

    output = LD_RequestLaserSetPoint(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestMaxCurrent = lib.LD_RequestMaxCurrent
LD_RequestMaxCurrent.restype = c_short
LD_RequestMaxCurrent.argtypes = [POINTER(c_char)]


def request_max_current(serial_number):
    # requests the maximum current dig pot position.

    serial_number = POINTER(c_char)

    output = LD_RequestMaxCurrent(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestRampupMode = lib.LD_RequestRampupMode
LD_RequestRampupMode.restype = c_short
LD_RequestRampupMode.argtypes = [POINTER(c_char)]


def request_rampup_mode(serial_number):
    # Requests the ramp up mode.

    serial_number = POINTER(c_char)

    output = LD_RequestRampupMode(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestReadings = lib.LD_RequestReadings
LD_RequestReadings.restype = c_short
LD_RequestReadings.argtypes = [POINTER(c_char)]


def request_readings(serial_number):
    # Request power and current readings.

    serial_number = POINTER(c_char)

    output = LD_RequestReadings(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestSettings = lib.LD_RequestSettings
LD_RequestSettings.restype = c_short
LD_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = LD_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestStatus = lib.LD_RequestStatus
LD_RequestStatus.restype = c_short
LD_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the state quantities (actual power, current and status).

    serial_number = POINTER(c_char)

    output = LD_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestStatusBits = lib.LD_RequestStatusBits
LD_RequestStatusBits.restype = c_short
LD_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = LD_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_RequestWACalibFactor = lib.LD_RequestWACalibFactor
LD_RequestWACalibFactor.restype = c_short
LD_RequestWACalibFactor.argtypes = [POINTER(c_char)]


def request_w_a_calib_factor(serial_number):
    # Requests the wa calib factor.

    serial_number = POINTER(c_char)

    output = LD_RequestWACalibFactor(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_SetClosedLoopMode = lib.LD_SetClosedLoopMode
LD_SetClosedLoopMode.restype = c_short
LD_SetClosedLoopMode.argtypes = [POINTER(c_char)]


def set_closed_loop_mode(serial_number):
    # Set closed loop mode.

    serial_number = POINTER(c_char)

    output = LD_SetClosedLoopMode(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_SetControlSource = lib.LD_SetControlSource
LD_SetControlSource.restype = c_short
LD_SetControlSource.argtypes = [POINTER(c_char), LD_InputSourceFlags]


def set_control_source(serial_number):
    # Sets the control input source.

    serial_number = POINTER(c_char)
    source = LD_InputSourceFlags()

    output = LD_SetControlSource(serial_number, source)
    if output != 0:
        raise KinesisException(output)


LD_SetDisplayUnits = lib.LD_SetDisplayUnits
LD_SetDisplayUnits.restype = c_short
LD_SetDisplayUnits.argtypes = [POINTER(c_char), LD_DisplayUnits]


def set_display_units(serial_number):
    # Sets the hardware display units.

    serial_number = POINTER(c_char)
    units = LD_DisplayUnits()

    output = LD_SetDisplayUnits(serial_number, units)
    if output != 0:
        raise KinesisException(output)


LD_SetFrontPanelLock = lib.LD_SetFrontPanelLock
LD_SetFrontPanelLock.restype = c_short
LD_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = LD_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


LD_SetLEDBrightness = lib.LD_SetLEDBrightness
LD_SetLEDBrightness.restype = c_short
LD_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = LD_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


LD_SetLaserPolarity = lib.LD_SetLaserPolarity
LD_SetLaserPolarity.restype = c_short
LD_SetLaserPolarity.argtypes = [POINTER(c_char), LD_POLARITY]


def set_laser_polarity(serial_number):
    # Sets the laser polarity.

    serial_number = POINTER(c_char)
    polarity = LD_POLARITY()

    output = LD_SetLaserPolarity(serial_number, polarity)
    if output != 0:
        raise KinesisException(output)


LD_SetLaserSetPoint = lib.LD_SetLaserSetPoint
LD_SetLaserSetPoint.restype = c_short
LD_SetLaserSetPoint.argtypes = [POINTER(c_char), c_long]


def set_laser_set_point(serial_number):
    # Sets the Laser Diode Current.

    serial_number = POINTER(c_char)
    laserDiodeCurrent = c_long()

    output = LD_SetLaserSetPoint(serial_number, laserDiodeCurrent)
    if output != 0:
        raise KinesisException(output)


LD_SetMaxCurrent = lib.LD_SetMaxCurrent
LD_SetMaxCurrent.restype = c_short
LD_SetMaxCurrent.argtypes = [POINTER(c_char), c_long]


def set_max_current(serial_number):
    # Sets the maximum current digital pot position.

    serial_number = POINTER(c_char)
    maxCurrent = c_long()

    output = LD_SetMaxCurrent(serial_number, maxCurrent)
    if output != 0:
        raise KinesisException(output)


LD_SetOpenLoopMode = lib.LD_SetOpenLoopMode
LD_SetOpenLoopMode.restype = c_short
LD_SetOpenLoopMode.argtypes = [POINTER(c_char)]


def set_open_loop_mode(serial_number):
    # Set open loop mode.

    serial_number = POINTER(c_char)

    output = LD_SetOpenLoopMode(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_SetRampupMode = lib.LD_SetRampupMode
LD_SetRampupMode.restype = c_short
LD_SetRampupMode.argtypes = [POINTER(c_char), KLD_RAMPUP]


def set_rampup_mode(serial_number):
    # Sets the laser ramp up mode.

    serial_number = POINTER(c_char)
    rampupMode = KLD_RAMPUP()

    output = LD_SetRampupMode(serial_number, rampupMode)
    if output != 0:
        raise KinesisException(output)


LD_SetWACalibFactor = lib.LD_SetWACalibFactor
LD_SetWACalibFactor.restype = c_short
LD_SetWACalibFactor.argtypes = [POINTER(c_char), c_float]


def set_w_a_calib_factor(serial_number):
    # Sets the W/A calibration factor.

    serial_number = POINTER(c_char)
    calibFactor = c_float()

    output = LD_SetWACalibFactor(serial_number, calibFactor)
    if output != 0:
        raise KinesisException(output)


LD_StartPolling = lib.LD_StartPolling
LD_StartPolling.restype = c_bool
LD_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = LD_StartPolling(serial_number, milliseconds)

    return output


LD_StopFindTIAGain = lib.LD_StopFindTIAGain
LD_StopFindTIAGain.restype = c_short
LD_StopFindTIAGain.argtypes = [POINTER(c_char)]


def stop_find_t_i_a_gain(serial_number):
    # Stopps the FindTIAGain calibration.

    serial_number = POINTER(c_char)

    output = LD_StopFindTIAGain(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_StopPolling = lib.LD_StopPolling
LD_StopPolling.restype = c_void_p
LD_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = LD_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


LD_TimeSinceLastMsgReceived = lib.LD_TimeSinceLastMsgReceived
LD_TimeSinceLastMsgReceived.restype = c_bool
LD_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = LD_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


LD_WaitForMessage = lib.LD_WaitForMessage
LD_WaitForMessage.restype = c_bool
LD_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = LD_WaitForMessage(serial_number, messageType, messageID, messageData)

    return output


LS_GetMMIParams = lib.LS_GetMMIParams
LS_GetMMIParams.restype = c_short
LS_GetMMIParams.argtypes = [POINTER(c_char)]


def get_m_m_i_params(serial_number):
    # Gets the MMI parameters.

    serial_number = POINTER(c_char)

    output = LS_GetMMIParams(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetMMIParamsBlock = lib.LS_GetMMIParamsBlock
LS_GetMMIParamsBlock.restype = c_short
LS_GetMMIParamsBlock.argtypes = [POINTER(c_char), KLD_MMIParams, KLS_MMIParams]


def get_m_m_i_params_block(serial_number):
    # Gets the MMI parameters.

    serial_number = POINTER(c_char)
    params = KLD_MMIParams()
    params = KLS_MMIParams()

    output = LS_GetMMIParamsBlock(serial_number, params, params)
    if output != 0:
        raise KinesisException(output)


LS_GetTrigIOParams = lib.LS_GetTrigIOParams
LS_GetTrigIOParams.restype = c_short
LS_GetTrigIOParams.argtypes = [
    POINTER(c_char),
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TrigPolarity,
    KLS_TrigPolarity,
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TrigPolarity,
    KLS_TrigPolarity]


def get_trig_i_o_params(serial_number):
    # Gets the Trigger IO parameters.

    serial_number = POINTER(c_char)
    mode1 = KLD_TriggerMode()
    mode1 = KLS_TriggerMode()
    polarity1 = KLD_TrigPolarity()
    polarity1 = KLS_TrigPolarity()
    mode2 = KLD_TriggerMode()
    mode2 = KLS_TriggerMode()
    polarity2 = KLD_TrigPolarity()
    polarity2 = KLS_TrigPolarity()

    output = LS_GetTrigIOParams(serial_number, mode1, mode1, polarity1, polarity1, mode2, mode2, polarity2, polarity2)
    if output != 0:
        raise KinesisException(output)


LS_GetTrigIOParamsBlock = lib.LS_GetTrigIOParamsBlock
LS_GetTrigIOParamsBlock.restype = c_short
LS_GetTrigIOParamsBlock.argtypes = [POINTER(c_char), KLD_TrigIOParams, KLS_TrigIOParams]


def get_trig_i_o_params_block(serial_number):
    # Gets the Trigger IO parameters.

    serial_number = POINTER(c_char)
    params = KLD_TrigIOParams()
    params = KLS_TrigIOParams()

    output = LS_GetTrigIOParamsBlock(serial_number, params, params)
    if output != 0:
        raise KinesisException(output)


LS_RequestMMIParams = lib.LS_RequestMMIParams
LS_RequestMMIParams.restype = c_short
LS_RequestMMIParams.argtypes = [POINTER(c_char)]


def request_m_m_i_params(serial_number):
    # Requests the MMI parameters.

    serial_number = POINTER(c_char)

    output = LS_RequestMMIParams(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestTrigIOParams = lib.LS_RequestTrigIOParams
LS_RequestTrigIOParams.restype = c_short
LS_RequestTrigIOParams.argtypes = [POINTER(c_char)]


def request_trig_i_o_params(serial_number):
    # Requests the Trigger IO parameters.

    serial_number = POINTER(c_char)

    output = LS_RequestTrigIOParams(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_SetMMIParams = lib.LS_SetMMIParams
LS_SetMMIParams.restype = c_short
LS_SetMMIParams.argtypes = [POINTER(c_char), c_short]


def set_m_m_i_params(serial_number):
    # Sets the MMI parameters.

    serial_number = POINTER(c_char)
    dispIntensity = c_short()

    output = LS_SetMMIParams(serial_number, dispIntensity)
    if output != 0:
        raise KinesisException(output)


LS_SetMMIParamsBlock = lib.LS_SetMMIParamsBlock
LS_SetMMIParamsBlock.restype = c_short
LS_SetMMIParamsBlock.argtypes = [POINTER(c_char), KLD_MMIParams, KLS_MMIParams]


def set_m_m_i_params_block(serial_number):
    # Sets the MMI parameters.

    serial_number = POINTER(c_char)
    params = KLD_MMIParams()
    params = KLS_MMIParams()

    output = LS_SetMMIParamsBlock(serial_number, params, params)
    if output != 0:
        raise KinesisException(output)


LS_SetTrigIOParams = lib.LS_SetTrigIOParams
LS_SetTrigIOParams.restype = c_short
LS_SetTrigIOParams.argtypes = [
    POINTER(c_char),
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TrigPolarity,
    KLS_TrigPolarity,
    KLD_TriggerMode,
    KLS_TriggerMode,
    KLD_TrigPolarity,
    KLS_TrigPolarity]


def set_trig_i_o_params(serial_number):
    # Sets the Trigger IO parameters.

    serial_number = POINTER(c_char)
    mode1 = KLD_TriggerMode()
    mode1 = KLS_TriggerMode()
    polarity1 = KLD_TrigPolarity()
    polarity1 = KLS_TrigPolarity()
    mode2 = KLD_TriggerMode()
    mode2 = KLS_TriggerMode()
    polarity2 = KLD_TrigPolarity()
    polarity2 = KLS_TrigPolarity()

    output = LS_SetTrigIOParams(serial_number, mode1, mode1, polarity1, polarity1, mode2, mode2, polarity2, polarity2)
    if output != 0:
        raise KinesisException(output)


LS_SetTrigIOParamsBlock = lib.LS_SetTrigIOParamsBlock
LS_SetTrigIOParamsBlock.restype = c_short
LS_SetTrigIOParamsBlock.argtypes = [POINTER(c_char), KLD_TrigIOParams, KLS_TrigIOParams]


def set_trig_i_o_params_block(serial_number):
    # Ls set trig i/o parameters block.

    serial_number = POINTER(c_char)
    params = KLD_TrigIOParams()
    params = KLS_TrigIOParams()

    output = LS_SetTrigIOParamsBlock(serial_number, params, params)
    if output != 0:
        raise KinesisException(output)


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
