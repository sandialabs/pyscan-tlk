from ctypes import (POINTER, c_bool, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    TIM_ButtonParameters,
    TIM_ButtonsMode,
    TIM_Channels,
    TIM_Direction,
    TIM_DriveOPParameters,
    TIM_JogMode,
    TIM_JogParameters)
from .definitions.structures import (TLI_DeviceInfo, TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.InertialMotor.DLL")

TIM_CheckConnection = lib.TIM_CheckConnection
TIM_CheckConnection.restype = c_bool
TIM_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = TIM_CheckConnection(serial_number)

    return output


TIM_ClearMessageQueue = lib.TIM_ClearMessageQueue
TIM_ClearMessageQueue.restype = c_void_p
TIM_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = TIM_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_Close = lib.TIM_Close
TIM_Close.restype = c_void_p
TIM_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = TIM_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_Disable = lib.TIM_Disable
TIM_Disable.restype = c_short
TIM_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable cube.

    serial_number = POINTER(c_char)

    output = TIM_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_Disconnect = lib.TIM_Disconnect
TIM_Disconnect.restype = c_short
TIM_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = TIM_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_Enable = lib.TIM_Enable
TIM_Enable.restype = c_short
TIM_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable cube for computer control.

    serial_number = POINTER(c_char)

    output = TIM_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_EnableLastMsgTimer = lib.TIM_EnableLastMsgTimer
TIM_EnableLastMsgTimer.restype = c_void_p
TIM_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = TIM_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


TIM_GetButtonParameters = lib.TIM_GetButtonParameters
TIM_GetButtonParameters.restype = c_short
TIM_GetButtonParameters.argtypes = [POINTER(c_char), TIM_Channels, TIM_ButtonsMode, c_int32, c_int32]


def get_button_parameters(serial_number, channel):
    # Gets a button parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    buttonMode = TIM_ButtonsMode()
    position1 = c_int32()
    position2 = c_int32()

    output = TIM_GetButtonParameters(serial_number, channel, buttonMode, position1, position2)
    if output != 0:
        raise KinesisException(output)


TIM_GetButtonParametersStruct = lib.TIM_GetButtonParametersStruct
TIM_GetButtonParametersStruct.restype = c_short
TIM_GetButtonParametersStruct.argtypes = [POINTER(c_char), TIM_Channels, TIM_ButtonParameters]


def get_button_parameters_struct(serial_number, channel):
    # Gets a button parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    buttonParameters = TIM_ButtonParameters()

    output = TIM_GetButtonParametersStruct(serial_number, channel, buttonParameters)
    if output != 0:
        raise KinesisException(output)


TIM_GetCurrentPosition = lib.TIM_GetCurrentPosition
TIM_GetCurrentPosition.restype = c_int32
TIM_GetCurrentPosition.argtypes = [POINTER(c_char), TIM_Channels]


def get_current_position(serial_number, channel):
    # Gets current position.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_GetCurrentPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_GetDriveOPParameters = lib.TIM_GetDriveOPParameters
TIM_GetDriveOPParameters.restype = c_short
TIM_GetDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels, c_int16, c_int32, c_int32]


def get_drive_o_p_parameters(serial_number, channel):
    # Gets the operation drive parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    maxVoltage = c_int16()
    stepRate = c_int32()
    stepAcceleration = c_int32()

    output = TIM_GetDriveOPParameters(serial_number, channel, maxVoltage, stepRate, stepAcceleration)
    if output != 0:
        raise KinesisException(output)


TIM_GetDriveOPParametersStruct = lib.TIM_GetDriveOPParametersStruct
TIM_GetDriveOPParametersStruct.restype = c_short
TIM_GetDriveOPParametersStruct.argtypes = [POINTER(c_char), TIM_Channels, TIM_DriveOPParameters]


def get_drive_o_p_parameters_struct(serial_number, channel):
    # Gets the operation drive parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    driveOPParameters = TIM_DriveOPParameters()

    output = TIM_GetDriveOPParametersStruct(serial_number, channel, driveOPParameters)
    if output != 0:
        raise KinesisException(output)


TIM_GetFirmwareVersion = lib.TIM_GetFirmwareVersion
TIM_GetFirmwareVersion.restype = c_ulong
TIM_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = TIM_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_GetHardwareInfo = lib.TIM_GetHardwareInfo
TIM_GetHardwareInfo.restype = c_short
TIM_GetHardwareInfo.argtypes = [
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

    output = TIM_GetHardwareInfo(
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


TIM_GetHardwareInfoBlock = lib.TIM_GetHardwareInfoBlock
TIM_GetHardwareInfoBlock.restype = c_short
TIM_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = TIM_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


TIM_GetJogParameters = lib.TIM_GetJogParameters
TIM_GetJogParameters.restype = c_short
TIM_GetJogParameters.argtypes = [POINTER(c_char), TIM_Channels, TIM_JogMode, c_int32, c_int32, c_int32]


def get_jog_parameters(serial_number, channel):
    # Gets the jog parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    jogMode = TIM_JogMode()
    jogStepSize = c_int32()
    jogStepRate = c_int32()
    jogStepAcceleration = c_int32()

    output = TIM_GetJogParameters(serial_number, channel, jogMode, jogStepSize, jogStepRate, jogStepAcceleration)
    if output != 0:
        raise KinesisException(output)


TIM_GetJogParametersStruct = lib.TIM_GetJogParametersStruct
TIM_GetJogParametersStruct.restype = c_short
TIM_GetJogParametersStruct.argtypes = [POINTER(c_char), TIM_Channels, TIM_JogParameters]


def get_jog_parameters_struct(serial_number, channel):
    # Gets the jog parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    jogParameters = TIM_JogParameters()

    output = TIM_GetJogParametersStruct(serial_number, channel, jogParameters)
    if output != 0:
        raise KinesisException(output)


TIM_GetLEDBrightness = lib.TIM_GetLEDBrightness
TIM_GetLEDBrightness.restype = c_short
TIM_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = TIM_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_GetMaxPotStepRate = lib.TIM_GetMaxPotStepRate
TIM_GetMaxPotStepRate.restype = c_int32
TIM_GetMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels]


def get_max_pot_step_rate(serial_number, channel):
    # Gets the maximum potentiometer step rate.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_GetMaxPotStepRate(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_GetNextMessage = lib.TIM_GetNextMessage
TIM_GetNextMessage.restype = c_bool
TIM_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = TIM_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


TIM_GetSoftwareVersion = lib.TIM_GetSoftwareVersion
TIM_GetSoftwareVersion.restype = c_ulong
TIM_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = TIM_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_GetStatusBits = lib.TIM_GetStatusBits
TIM_GetStatusBits.restype = c_ulong
TIM_GetStatusBits.argtypes = [POINTER(c_char), TIM_Channels]


def get_status_bits(serial_number, channel):
    # Tc get status bits.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_GetStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_HasLastMsgTimerOverrun = lib.TIM_HasLastMsgTimerOverrun
TIM_HasLastMsgTimerOverrun.restype = c_bool
TIM_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by TIM_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = TIM_HasLastMsgTimerOverrun(serial_number)

    return output


TIM_Home = lib.TIM_Home
TIM_Home.restype = c_short
TIM_Home.argtypes = [POINTER(c_char), TIM_Channels]


def home(serial_number, channel):
    # Sets the current position to the Home position (Position = 0).

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_Home(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_Identify = lib.TIM_Identify
TIM_Identify.restype = c_void_p
TIM_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = TIM_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_LoadNamedSettings = lib.TIM_LoadNamedSettings
TIM_LoadNamedSettings.restype = c_bool
TIM_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = TIM_LoadNamedSettings(serial_number, settingsName)

    return output


TIM_LoadSettings = lib.TIM_LoadSettings
TIM_LoadSettings.restype = c_bool
TIM_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = TIM_LoadSettings(serial_number)

    return output


TIM_MessageQueueSize = lib.TIM_MessageQueueSize
TIM_MessageQueueSize.restype = c_int
TIM_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = TIM_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_MoveAbsolute = lib.TIM_MoveAbsolute
TIM_MoveAbsolute.restype = c_short
TIM_MoveAbsolute.argtypes = [POINTER(c_char), TIM_Channels, c_int32]


def move_absolute(serial_number, channel):
    # Move absolute.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    position = c_int32()

    output = TIM_MoveAbsolute(serial_number, channel, position)
    if output != 0:
        raise KinesisException(output)


TIM_MoveJog = lib.TIM_MoveJog
TIM_MoveJog.restype = c_short
TIM_MoveJog.argtypes = [POINTER(c_char), TIM_Channels, TIM_Direction]


def move_jog(serial_number, channel):
    # Move jog.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    jogDirection = TIM_Direction()

    output = TIM_MoveJog(serial_number, channel, jogDirection)
    if output != 0:
        raise KinesisException(output)


TIM_MoveStop = lib.TIM_MoveStop
TIM_MoveStop.restype = c_short
TIM_MoveStop.argtypes = [POINTER(c_char), TIM_Channels]


def move_stop(serial_number, channel):
    # Move stop.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_MoveStop(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_Open = lib.TIM_Open
TIM_Open.restype = c_short
TIM_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = TIM_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_PersistSettings = lib.TIM_PersistSettings
TIM_PersistSettings.restype = c_bool
TIM_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = TIM_PersistSettings(serial_number)

    return output


TIM_PollingDuration = lib.TIM_PollingDuration
TIM_PollingDuration.restype = c_long
TIM_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = TIM_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_RegisterMessageCallback = lib.TIM_RegisterMessageCallback
TIM_RegisterMessageCallback.restype = c_void_p
TIM_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = TIM_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


TIM_RequestButtonParameters = lib.TIM_RequestButtonParameters
TIM_RequestButtonParameters.restype = c_short
TIM_RequestButtonParameters.argtypes = [POINTER(c_char), TIM_Channels]


def request_button_parameters(serial_number, channel):
    # Requests the button parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_RequestButtonParameters(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_RequestCurrentPosition = lib.TIM_RequestCurrentPosition
TIM_RequestCurrentPosition.restype = c_short
TIM_RequestCurrentPosition.argtypes = [POINTER(c_char), TIM_Channels]


def request_current_position(serial_number, channel):
    # Requests the current position.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_RequestCurrentPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_RequestDriveOPParameters = lib.TIM_RequestDriveOPParameters
TIM_RequestDriveOPParameters.restype = c_short
TIM_RequestDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels]


def request_drive_o_p_parameters(serial_number, channel):
    # Requests the operation drive parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_RequestDriveOPParameters(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_RequestJogParameters = lib.TIM_RequestJogParameters
TIM_RequestJogParameters.restype = c_short
TIM_RequestJogParameters.argtypes = [POINTER(c_char), TIM_Channels]


def request_jog_parameters(serial_number, channel):
    # Requests the jog parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_RequestJogParameters(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_RequestMaxPotStepRate = lib.TIM_RequestMaxPotStepRate
TIM_RequestMaxPotStepRate.restype = c_short
TIM_RequestMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels]


def request_max_pot_step_rate(serial_number, channel):
    # Requests the maximum potentiometer step rate.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()

    output = TIM_RequestMaxPotStepRate(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


TIM_RequestSettings = lib.TIM_RequestSettings
TIM_RequestSettings.restype = c_short
TIM_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = TIM_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_RequestStatus = lib.TIM_RequestStatus
TIM_RequestStatus.restype = c_short
TIM_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the state quantities (actual temperature, current and status bits).

    serial_number = POINTER(c_char)

    output = TIM_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_RequestStatusBits = lib.TIM_RequestStatusBits
TIM_RequestStatusBits.restype = c_short
TIM_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = TIM_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_Reset = lib.TIM_Reset
TIM_Reset.restype = c_short
TIM_Reset.argtypes = [POINTER(c_char)]


def reset(serial_number):
    # Reset the device.

    serial_number = POINTER(c_char)

    output = TIM_Reset(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_SetButtonParameters = lib.TIM_SetButtonParameters
TIM_SetButtonParameters.restype = c_short
TIM_SetButtonParameters.argtypes = [POINTER(c_char), TIM_Channels, TIM_ButtonsMode, c_int32, c_int32]


def set_button_parameters(serial_number, channel):
    # Sets a button parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    buttonMode = TIM_ButtonsMode()
    position1 = c_int32()
    position2 = c_int32()

    output = TIM_SetButtonParameters(serial_number, channel, buttonMode, position1, position2)
    if output != 0:
        raise KinesisException(output)


TIM_SetButtonParametersStruct = lib.TIM_SetButtonParametersStruct
TIM_SetButtonParametersStruct.restype = c_short
TIM_SetButtonParametersStruct.argtypes = [POINTER(c_char), TIM_Channels, TIM_ButtonParameters]


def set_button_parameters_struct(serial_number, channel):
    # Sets a button parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    buttonParameters = TIM_ButtonParameters()

    output = TIM_SetButtonParametersStruct(serial_number, channel, buttonParameters)
    if output != 0:
        raise KinesisException(output)


TIM_SetDriveOPParameters = lib.TIM_SetDriveOPParameters
TIM_SetDriveOPParameters.restype = c_short
TIM_SetDriveOPParameters.argtypes = [POINTER(c_char), TIM_Channels, c_int16, c_int32, c_int32]


def set_drive_o_p_parameters(serial_number, channel):
    # Sets the operation drive parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    maxVoltage = c_int16()
    stepRate = c_int32()
    stepAcceleration = c_int32()

    output = TIM_SetDriveOPParameters(serial_number, channel, maxVoltage, stepRate, stepAcceleration)
    if output != 0:
        raise KinesisException(output)


TIM_SetDriveOPParametersStruct = lib.TIM_SetDriveOPParametersStruct
TIM_SetDriveOPParametersStruct.restype = c_short
TIM_SetDriveOPParametersStruct.argtypes = [POINTER(c_char), TIM_Channels, TIM_DriveOPParameters]


def set_drive_o_p_parameters_struct(serial_number, channel):
    # Sets the operation drive parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    driveOPParameters = TIM_DriveOPParameters()

    output = TIM_SetDriveOPParametersStruct(serial_number, channel, driveOPParameters)
    if output != 0:
        raise KinesisException(output)


TIM_SetJogParameters = lib.TIM_SetJogParameters
TIM_SetJogParameters.restype = c_short
TIM_SetJogParameters.argtypes = [POINTER(c_char), TIM_Channels, TIM_JogMode, c_int32, c_int32, c_int32]


def set_jog_parameters(serial_number, channel):
    # Sets the jog parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    jogMode = TIM_JogMode()
    jogStepSize = c_int32()
    jogStepRate = c_int32()
    jogStepAcceleration = c_int32()

    output = TIM_SetJogParameters(serial_number, channel, jogMode, jogStepSize, jogStepRate, jogStepAcceleration)
    if output != 0:
        raise KinesisException(output)


TIM_SetJogParametersStruct = lib.TIM_SetJogParametersStruct
TIM_SetJogParametersStruct.restype = c_short
TIM_SetJogParametersStruct.argtypes = [POINTER(c_char), TIM_Channels, TIM_JogParameters]


def set_jog_parameters_struct(serial_number, channel):
    # Sets the jog parameters.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    jogParameters = TIM_JogParameters()

    output = TIM_SetJogParametersStruct(serial_number, channel, jogParameters)
    if output != 0:
        raise KinesisException(output)


TIM_SetLEDBrightness = lib.TIM_SetLEDBrightness
TIM_SetLEDBrightness.restype = c_short
TIM_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = TIM_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


TIM_SetMaxPotStepRate = lib.TIM_SetMaxPotStepRate
TIM_SetMaxPotStepRate.restype = c_short
TIM_SetMaxPotStepRate.argtypes = [POINTER(c_char), TIM_Channels, c_int32]


def set_max_pot_step_rate(serial_number, channel):
    # Sets a maximum pot step rate.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    maxPotStepRate = c_int32()

    output = TIM_SetMaxPotStepRate(serial_number, channel, maxPotStepRate)
    if output != 0:
        raise KinesisException(output)


TIM_SetPosition = lib.TIM_SetPosition
TIM_SetPosition.restype = c_short
TIM_SetPosition.argtypes = [POINTER(c_char), TIM_Channels, c_long]


def set_position(serial_number, channel):
    # set the position.

    serial_number = POINTER(c_char)
    channel = TIM_Channels()
    position = c_long()

    output = TIM_SetPosition(serial_number, channel, position)
    if output != 0:
        raise KinesisException(output)


TIM_StartPolling = lib.TIM_StartPolling
TIM_StartPolling.restype = c_bool
TIM_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = TIM_StartPolling(serial_number, milliseconds)

    return output


TIM_StopPolling = lib.TIM_StopPolling
TIM_StopPolling.restype = c_void_p
TIM_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = TIM_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


TIM_TimeSinceLastMsgReceived = lib.TIM_TimeSinceLastMsgReceived
TIM_TimeSinceLastMsgReceived.restype = c_bool
TIM_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = TIM_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


TIM_WaitForMessage = lib.TIM_WaitForMessage
TIM_WaitForMessage.restype = c_bool
TIM_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = TIM_WaitForMessage(serial_number, messageType, messageID, messageData)

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
