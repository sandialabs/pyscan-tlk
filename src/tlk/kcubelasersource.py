from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KLD_TrigPolarity,
    KLD_TriggerMode,
    KLS_OpMode,
    KLS_TrigPolarity,
    KLS_TriggerMode,
    LS_InputSourceFlags)
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
    lib_path + "Thorlabs.MotionControl.KCube.LaserSource.DLL")

LS_CanDeviceLockFrontPanel = lib.LS_CanDeviceLockFrontPanel
LS_CanDeviceLockFrontPanel.restype = c_bool
LS_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = LS_CanDeviceLockFrontPanel(serial_number)

    return output


LS_CheckConnection = lib.LS_CheckConnection
LS_CheckConnection.restype = c_bool
LS_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = LS_CheckConnection(serial_number)

    return output


LS_ClearMessageQueue = lib.LS_ClearMessageQueue
LS_ClearMessageQueue.restype = c_void_p
LS_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = LS_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_Close = lib.LS_Close
LS_Close.restype = c_void_p
LS_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = LS_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_Disable = lib.LS_Disable
LS_Disable.restype = c_short
LS_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable laser.

    serial_number = POINTER(c_char)

    output = LS_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_DisableOutput = lib.LS_DisableOutput
LS_DisableOutput.restype = c_short
LS_DisableOutput.argtypes = [POINTER(c_char)]


def disable_output(serial_number):
    # Switch laser off.

    serial_number = POINTER(c_char)

    output = LS_DisableOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_Enable = lib.LS_Enable
LS_Enable.restype = c_short
LS_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable laser for computer control.

    serial_number = POINTER(c_char)

    output = LS_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_EnableLastMsgTimer = lib.LS_EnableLastMsgTimer
LS_EnableLastMsgTimer.restype = c_void_p
LS_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = LS_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


LS_EnableOutput = lib.LS_EnableOutput
LS_EnableOutput.restype = c_short
LS_EnableOutput.argtypes = [POINTER(c_char)]


def enable_output(serial_number):
    # Switch laser on.

    serial_number = POINTER(c_char)

    output = LS_EnableOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetControlSource = lib.LS_GetControlSource
LS_GetControlSource.restype = LS_InputSourceFlags
LS_GetControlSource.argtypes = [POINTER(c_char)]


def get_control_source(serial_number):
    # Gets the control input source.

    serial_number = POINTER(c_char)

    output = LS_GetControlSource(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetCurrentReading = lib.LS_GetCurrentReading
LS_GetCurrentReading.restype = c_long
LS_GetCurrentReading.argtypes = [POINTER(c_char)]


def get_current_reading(serial_number):
    # Gets current Current reading.

    serial_number = POINTER(c_char)

    output = LS_GetCurrentReading(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetFirmwareVersion = lib.LS_GetFirmwareVersion
LS_GetFirmwareVersion.restype = c_ulong
LS_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = LS_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetFrontPanelLocked = lib.LS_GetFrontPanelLocked
LS_GetFrontPanelLocked.restype = c_bool
LS_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = LS_GetFrontPanelLocked(serial_number)

    return output


LS_GetHardwareInfo = lib.LS_GetHardwareInfo
LS_GetHardwareInfo.restype = c_short
LS_GetHardwareInfo.argtypes = [
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

    output = LS_GetHardwareInfo(
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


LS_GetHardwareInfoBlock = lib.LS_GetHardwareInfoBlock
LS_GetHardwareInfoBlock.restype = c_short
LS_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = LS_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


LS_GetInterlockState = lib.LS_GetInterlockState
LS_GetInterlockState.restype = c_byte
LS_GetInterlockState.argtypes = [POINTER(c_char)]


def get_interlock_state(serial_number):
    # Gets the Interlock State.

    serial_number = POINTER(c_char)

    output = LS_GetInterlockState(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetLimits = lib.LS_GetLimits
LS_GetLimits.restype = c_short
LS_GetLimits.argtypes = [POINTER(c_char), c_long, c_long]


def get_limits(serial_number):
    # Gets the max power and current limits for the device.

    serial_number = POINTER(c_char)
    maxPower = c_long()
    maxCurrent = c_long()

    output = LS_GetLimits(serial_number, maxPower, maxCurrent)
    if output != 0:
        raise KinesisException(output)


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


LS_GetNextMessage = lib.LS_GetNextMessage
LS_GetNextMessage.restype = c_bool
LS_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = LS_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


LS_GetOPMode = lib.LS_GetOPMode
LS_GetOPMode.restype = c_short
LS_GetOPMode.argtypes = [POINTER(c_char), KLS_OpMode]


def get_o_p_mode(serial_number):
    # Gets the Operation Mode parameters.

    serial_number = POINTER(c_char)
    mode = KLS_OpMode()

    output = LS_GetOPMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


LS_GetPowerReading = lib.LS_GetPowerReading
LS_GetPowerReading.restype = c_long
LS_GetPowerReading.argtypes = [POINTER(c_char)]


def get_power_reading(serial_number):
    # Gets current power reading.

    serial_number = POINTER(c_char)

    output = LS_GetPowerReading(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetPowerSet = lib.LS_GetPowerSet
LS_GetPowerSet.restype = c_long
LS_GetPowerSet.argtypes = [POINTER(c_char)]


def get_power_set(serial_number):
    # Gets the output power currently set.

    serial_number = POINTER(c_char)

    output = LS_GetPowerSet(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetSoftwareVersion = lib.LS_GetSoftwareVersion
LS_GetSoftwareVersion.restype = c_ulong
LS_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = LS_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_GetStatusBits = lib.LS_GetStatusBits
LS_GetStatusBits.restype = c_ulong
LS_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = LS_GetStatusBits(serial_number)
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


LS_GetWavelength = lib.LS_GetWavelength
LS_GetWavelength.restype = c_long
LS_GetWavelength.argtypes = [POINTER(c_char)]


def get_wavelength(serial_number):
    # Gets the operating wavelength.

    serial_number = POINTER(c_char)

    output = LS_GetWavelength(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_HasLastMsgTimerOverrun = lib.LS_HasLastMsgTimerOverrun
LS_HasLastMsgTimerOverrun.restype = c_bool
LS_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by LS_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = LS_HasLastMsgTimerOverrun(serial_number)

    return output


LS_Identify = lib.LS_Identify
LS_Identify.restype = c_void_p
LS_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = LS_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_LoadNamedSettings = lib.LS_LoadNamedSettings
LS_LoadNamedSettings.restype = c_bool
LS_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = LS_LoadNamedSettings(serial_number, settingsName)

    return output


LS_LoadSettings = lib.LS_LoadSettings
LS_LoadSettings.restype = c_bool
LS_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = LS_LoadSettings(serial_number)

    return output


LS_MessageQueueSize = lib.LS_MessageQueueSize
LS_MessageQueueSize.restype = c_int
LS_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = LS_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_Open = lib.LS_Open
LS_Open.restype = c_short
LS_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = LS_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_PersistSettings = lib.LS_PersistSettings
LS_PersistSettings.restype = c_bool
LS_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = LS_PersistSettings(serial_number)

    return output


LS_PollingDuration = lib.LS_PollingDuration
LS_PollingDuration.restype = c_long
LS_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = LS_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RegisterMessageCallback = lib.LS_RegisterMessageCallback
LS_RegisterMessageCallback.restype = c_void_p
LS_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = LS_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


LS_RequestControlSource = lib.LS_RequestControlSource
LS_RequestControlSource.restype = c_short
LS_RequestControlSource.argtypes = [POINTER(c_char)]


def request_control_source(serial_number):
    # Gets the control input source.

    serial_number = POINTER(c_char)

    output = LS_RequestControlSource(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestFrontPanelLocked = lib.LS_RequestFrontPanelLocked
LS_RequestFrontPanelLocked.restype = c_short
LS_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = LS_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestLimits = lib.LS_RequestLimits
LS_RequestLimits.restype = c_short
LS_RequestLimits.argtypes = [POINTER(c_char)]


def request_limits(serial_number):
    # Requests the limits MaxPower and MaxCurrent.

    serial_number = POINTER(c_char)

    output = LS_RequestLimits(serial_number)
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


LS_RequestOPMode = lib.LS_RequestOPMode
LS_RequestOPMode.restype = c_short
LS_RequestOPMode.argtypes = [POINTER(c_char)]


def request_o_p_mode(serial_number):
    # Requests the Operation Mode parameters.

    serial_number = POINTER(c_char)

    output = LS_RequestOPMode(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestReadings = lib.LS_RequestReadings
LS_RequestReadings.restype = c_short
LS_RequestReadings.argtypes = [POINTER(c_char)]


def request_readings(serial_number):
    # Request power and current readings.

    serial_number = POINTER(c_char)

    output = LS_RequestReadings(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestSetPower = lib.LS_RequestSetPower
LS_RequestSetPower.restype = c_short
LS_RequestSetPower.argtypes = [POINTER(c_char)]


def request_set_power(serial_number):
    # Sets the output power.

    serial_number = POINTER(c_char)

    output = LS_RequestSetPower(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestSettings = lib.LS_RequestSettings
LS_RequestSettings.restype = c_short
LS_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = LS_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestStatus = lib.LS_RequestStatus
LS_RequestStatus.restype = c_short
LS_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the state quantities (actual power, current and status).

    serial_number = POINTER(c_char)

    output = LS_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_RequestStatusBits = lib.LS_RequestStatusBits
LS_RequestStatusBits.restype = c_short
LS_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = LS_RequestStatusBits(serial_number)
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


LS_RequestWavelength = lib.LS_RequestWavelength
LS_RequestWavelength.restype = c_short
LS_RequestWavelength.argtypes = [POINTER(c_char)]


def request_wavelength(serial_number):
    # Requests the device Wavelength.

    serial_number = POINTER(c_char)

    output = LS_RequestWavelength(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_SetControlSource = lib.LS_SetControlSource
LS_SetControlSource.restype = c_short
LS_SetControlSource.argtypes = [POINTER(c_char), LS_InputSourceFlags]


def set_control_source(serial_number):
    # Sets the control input source.

    serial_number = POINTER(c_char)
    source = LS_InputSourceFlags()

    output = LS_SetControlSource(serial_number, source)
    if output != 0:
        raise KinesisException(output)


LS_SetFrontPanelLock = lib.LS_SetFrontPanelLock
LS_SetFrontPanelLock.restype = c_short
LS_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = LS_SetFrontPanelLock(serial_number, locked)
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


LS_SetOPMode = lib.LS_SetOPMode
LS_SetOPMode.restype = c_short
LS_SetOPMode.argtypes = [POINTER(c_char), KLS_OpMode]


def set_o_p_mode(serial_number):
    # Sets the Operation Mode parameters.

    serial_number = POINTER(c_char)
    mode = KLS_OpMode()

    output = LS_SetOPMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


LS_SetPower = lib.LS_SetPower
LS_SetPower.restype = c_short
LS_SetPower.argtypes = [POINTER(c_char), c_long]


def set_power(serial_number):
    # Sets the output power.

    serial_number = POINTER(c_char)
    power = c_long()

    output = LS_SetPower(serial_number, power)
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


LS_StartPolling = lib.LS_StartPolling
LS_StartPolling.restype = c_bool
LS_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = LS_StartPolling(serial_number, milliseconds)

    return output


LS_StopPolling = lib.LS_StopPolling
LS_StopPolling.restype = c_void_p
LS_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = LS_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


LS_TimeSinceLastMsgReceived = lib.LS_TimeSinceLastMsgReceived
LS_TimeSinceLastMsgReceived.restype = c_bool
LS_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = LS_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


LS_WaitForMessage = lib.LS_WaitForMessage
LS_WaitForMessage.restype = c_bool
LS_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = LS_WaitForMessage(serial_number, messageType, messageID, messageData)

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
