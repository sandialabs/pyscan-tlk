from ctypes import (POINTER, pointer, c_bool, c_char, c_int, c_int32,
                    c_int64, c_long, c_short, c_ulong, c_void_p,
                    cdll, c_char_p)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (HubAnalogueModes, PZ_ControlModeTypes, PZ_InputSourceFlags)
from .definitions.structures import (
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation,
    TPZ_IOSettings)
from .definitions.kinesisexception import KinesisException

# CUSTOM TYPES
c_short_p = type(pointer(c_short()))
c_ulong_p = type(pointer(c_ulong()))
c_long_p = type(pointer(c_long()))

lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.Piezo.DLL")

PCC_CheckConnection = lib.PCC_CheckConnection
PCC_CheckConnection.restype = c_bool
PCC_CheckConnection.argtypes = [POINTER(c_char)]


# Check settings, open and close device

def check_connection(serial_number):
    # Check connection.
    # Returns bool
    # tested and working 7/11/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_CheckConnection(serial_number)

    return output


PCC_ClearMessageQueue = lib.PCC_ClearMessageQueue
PCC_ClearMessageQueue.restype = c_void_p
PCC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.
    # Returns None
    # tested and working 7/11/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    _ = PCC_ClearMessageQueue(serial_number)


PCC_Open = lib.PCC_Open
PCC_Open.restype = c_short
PCC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.
    # Returns None; Raises exception on error
    # Tested and working 8/16/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_Open(serial_number)

    if output != 0:
        raise KinesisException(output)


PCC_Close = lib.PCC_Close
PCC_Close.restype = c_void_p
PCC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.
    # Returns None
    # tested and working 7/11/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    _ = PCC_Close(serial_number)


PCC_Disable = lib.PCC_Disable
PCC_Disable.restype = c_short
PCC_Disable.argtypes = [POINTER(c_char)]

# Disable/enable


def disable(serial_number):
    # Disable the cube.
    # Returns None; raises exception upon error
    # Untested

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_Enable = lib.PCC_Enable
PCC_Enable.restype = c_short
PCC_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable cube for computer control.
    # Returns None; raises exception upon error
    # Untested
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


# Voltage settings
# Max voltage
PCC_GetMaxOutputVoltage = lib.PCC_GetMaxOutputVoltage
PCC_GetMaxOutputVoltage.restype = c_short
PCC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_max_output_voltage(serial_number):
    # Gets the maximum output voltage.
    # The maximum output voltage, 750, 1000 or 1500 (75.0, 100.0, 150.0).
    # tested and working 7/11/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetMaxOutputVoltage(serial_number)

    return output


PCC_SetMaxOutputVoltage = lib.PCC_SetMaxOutputVoltage
PCC_SetMaxOutputVoltage.restype = c_short
PCC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]


def set_max_output_voltage(serial_number, maxVoltage):
    # Sets the maximum output voltage.
    # maxVoltage is The maximum output voltage, 750, 1000 or 1500 (75.0, 100.0, 150.0). 
    # Returns None; raises exception upon error
    # Tested and working 08/16/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    maxVoltage = c_short(maxVoltage)

    output = PCC_SetMaxOutputVoltage(serial_number, maxVoltage)
    if output != 0:
        raise KinesisException(output)


PCC_GetOutputVoltage = lib.PCC_GetOutputVoltage
PCC_GetOutputVoltage.restype = c_short
PCC_GetOutputVoltage.argtypes = [POINTER(c_char)]

# Voltage output


def get_output_voltage(serial_number):
    # Gets the set Output Voltage.
    # Returns the voltage as a percentage of MaxOutputVoltage, range -32767 to 32767 equivalent to -100% to 100%. 
    # Tested and working 8/16/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetOutputVoltage(serial_number)

    return output


PCC_SetOutputVoltage = lib.PCC_SetOutputVoltage
PCC_SetOutputVoltage.restype = c_short
PCC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]


def set_output_voltage(serial_number, volts):
    # Sets the output voltage.
    # volts is a percentage of MaxOutputVoltage, range -32767 to 32767 equivalent to -100% to 100%. 
    # Returns None; raises exception upon error
    # Tested and working 8/16/2024. Sometimes has to be run twice?

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    volts = c_short(volts)

    output = PCC_SetOutputVoltage(serial_number, volts)

    if output != 0:
        raise KinesisException(output)


PCC_Disconnect = lib.PCC_Disconnect
PCC_Disconnect.restype = c_short
PCC_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.
    # Returns None; raises exception upon error

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_EnableLastMsgTimer = lib.PCC_EnableLastMsgTimer
PCC_EnableLastMsgTimer.restype = c_void_p
PCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number, enable, lastMsgTimeout):
    # Enables the last message monitoring timer.
    # Untested

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    enable = c_bool(enable)
    lastMsgTimeout = c_int32(lastMsgTimeout)

    _ = PCC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)



PCC_GetFeedbackLoopPIconsts = lib.PCC_GetFeedbackLoopPIconsts
PCC_GetFeedbackLoopPIconsts.restype = c_short
PCC_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short_p, c_short_p]


def get_feedback_loop_pi_consts(serial_number):
    # Gets the feedback loop parameters and returns a tuple
    # Tested and working 8/16/2024
    
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalTerm = pointer(c_short())
    integralTerm = pointer(c_short())

    output = PCC_GetFeedbackLoopPIconsts(serial_number, proportionalTerm, integralTerm)
    if output != 0:
        raise KinesisException(output)
    return proportionalTerm.contents.value, integralTerm.contents.value



PCC_GetFeedbackLoopPIconstsBlock = lib.PCC_GetFeedbackLoopPIconstsBlock
PCC_GetFeedbackLoopPIconstsBlock.restype = c_short
PCC_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char), PZ_FeedbackLoopConstants]


def get_feedback_loop_pi_consts_block(serial_number):
    # Gets the feedback loop constants in a block.
    # Not implemented

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PCC_GetFeedbackLoopPIconstsBlock(serial_number, proportionalAndIntegralConstants)
    if output != 0:
        raise KinesisException(output)


PCC_GetFirmwareVersion = lib.PCC_GetFirmwareVersion
PCC_GetFirmwareVersion.restype = c_ulong
PCC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.
    # Tested and working 8/16/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetFirmwareVersion(serial_number)
    return output


PCC_GetHardwareInfo = lib.PCC_GetHardwareInfo
PCC_GetHardwareInfo.restype = c_short
PCC_GetHardwareInfo.argtypes = [
    c_char_p,
    c_char_p,
    c_ulong,
    c_long_p,
    c_long_p,
    c_char_p,
    c_ulong,
    c_ulong_p,
    c_long_p,
    c_long_p]

from time import sleep
def get_hardware_info(serial_number):
    # Gets the hardware information from the device.
    # Tested and working 8/16/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    modelNo = c_char_p()
    sizeOfModelNo = c_ulong(8)
    hardware_type = pointer(c_long())
    numChannels = pointer(c_long())
    notes = c_char_p()
    sizeOfNotes = c_ulong(48)
    firmwareVersion = pointer(c_ulong())
    hardwareVersion = pointer(c_long())
    modificationState = pointer(c_long())

    output = PCC_GetHardwareInfo(
        serial_number,
        modelNo,
        sizeOfModelNo,
        hardware_type,
        numChannels,
        notes,
        sizeOfNotes,
        firmwareVersion,
        hardwareVersion,
        modificationState)
    if output != 0:
        raise KinesisException(output)
    
    sleep(0.5)
    return {"serial_number": int(serial_number.value),
            "modelNo": modelNo.value,
            "type": hardware_type.contents.value,
            "numChannels": numChannels.contents.value,
            "notes": notes.value,
            "firmwareVersion": firmwareVersion.contents.value,
            "hardwareVersion": hardwareVersion.contents.value,
            "modificationState": modificationState.contents.value
            }


PCC_GetHardwareInfoBlock = lib.PCC_GetHardwareInfoBlock
PCC_GetHardwareInfoBlock.restype = c_short
PCC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.
    # Not implemented

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hardwareInfo = TLI_HardwareInformation()

    output = PCC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


PCC_GetHubAnalogInput = lib.PCC_GetHubAnalogInput
PCC_GetHubAnalogInput.restype = HubAnalogueModes
PCC_GetHubAnalogInput.argtypes = [POINTER(c_char)]


def get_hub_analog_input(serial_number):
    # Gets the Hub Analog Input.
    # Returns Hub Analogue Input Mode. 
    # Input applied to all Hub bays 1  
    # Input applied to adjacent Hub bays 2  
    # Input is from external SMA 3  

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetHubAnalogInput(serial_number)
    return output


PCC_GetIOSettings = lib.PCC_GetIOSettings
PCC_GetIOSettings.restype = TPZ_IOSettings
PCC_GetIOSettings.argtypes = [POINTER(c_char)]


def get_i_o_settings(serial_number):
    # Gets the IO settings.
    # Returns The settings as a TPZ_IOSettings structure
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetIOSettings(serial_number)
    return {"hubAnalogueInput": output.hubAnalogueInput,
            "maximumOutputVoltage": output.maximumOutputVoltage
            }


PCC_GetLEDBrightness = lib.PCC_GetLEDBrightness
PCC_GetLEDBrightness.restype = c_short
PCC_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_led_brightness(serial_number):
    # Gets the LED brightness.
    # Returns Intensity from 0 (off) to 255. 
    # Tested and working 8/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetLEDBrightness(serial_number)
    return output


PCC_GetNextMessage = lib.PCC_GetNextMessage
PCC_GetNextMessage.restype = c_bool
PCC_GetNextMessage.argtypes = [POINTER(c_char), c_long_p, c_long_p, c_ulong_p]


def get_next_message(serial_number):
    # Get the next MessageQueue item.
    # Tested and working 08/19/2024
    # Future feature: link the messageType codes and ID to 
    # words (table is in kinesis docs)
    
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = pointer(c_long())
    messageID = pointer(c_long())
    messageData = pointer(c_ulong())

    output = PCC_GetNextMessage(serial_number, messageType, messageID, messageData)
    # output is true if successful, false if not

    if output:
        return {
            "messageType": messageType.contents.value,
            "messageID": messageID.contents.value,
            "messageData": messageData.contents.value
        }


PCC_GetPosition = lib.PCC_GetPosition
PCC_GetPosition.restype = c_long
PCC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Gets the position when in closed loop mode.
    # ReturnsThe position as a percentage of maximum travel,
    # range 0 to 65535, equivalent to 0 to 100%.
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetPosition(serial_number)
    return output


PCC_GetPositionControlMode = lib.PCC_GetPositionControlMode
PCC_GetPositionControlMode.restype = PZ_ControlModeTypes
PCC_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode(serial_number):
    # Gets the Position Control Mode.
    # ReturnsThe control mode 
    #  Open Loop 1  
    #  Closed Loop 2  
    #  Open Loop smoothed 3  
    #  Closed Loop smoothed 4  
    # Tested and wroking 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetPositionControlMode(serial_number)
    return output

PCC_GetSoftwareVersion = lib.PCC_GetSoftwareVersion
PCC_GetSoftwareVersion.restype = c_ulong
PCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.
    # ReturnsThe device software version number made up of 4 byte parts. 
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetSoftwareVersion(serial_number)
    return output

PCC_GetStatusBits = lib.PCC_GetStatusBits
PCC_GetStatusBits.restype = c_ulong
PCC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.
    # 0x00000001 Piezo actuator connected (1=Connected, 0=Not connected).  
    # 0x00000002 For Future Use.  
    # 0x00000004 For Future Use.  
    # 0x00000008 For Future Use.  
    # 0x00000010 Piezo channel has been zeroed (1=Zeroed, 0=Not zeroed).  
    # 0x00000020 Piezo channel is zeroing (1=Zeroing, 0=Not zeroing).  
    # 0x00000040 For Future Use.  
    # 0x00000080 For Future Use.  
    # 0x00000100 Strain gauge feedback connected (1=Connected, 0=Not connected).  
    # 0x00000200 For Future Use.  
    # 0x00000400 Position control mode (1=Closed loop, 0=Open loop).  
    # 0x00000800 For Future Use.  
    # 0x00001000  
    # ...  
    # 0x00080000  
    # 0x00100000 Digital input 1 state (1=Logic High, 0=Logic Low).  
    # 0x00200000 Digital input 2 state (1=Logic High, 0=Logic Low).  
    # 0x00400000 Digital input 3 state (1=Logic High, 0=Logic Low).  
    # 0x00800000 Digital input 4 state (1=Logic High, 0=Logic Low).  
    # 0x01000000 Digital input 5 state (1=Logic High, 0=Logic Low).  
    # 0x02000000 Digital input 6 state (1=Logic High, 0=Logic Low).  
    # 0x04000000 Digital input 7 state (1=Logic High, 0=Logic Low).  
    # 0x08000000 Digital input 8 state (1=Logic High, 0=Logic Low).  
    # 0x10000000 For Future Use.  
    # 0x20000000 Active (1=Indicates Unit Is Active, 0=Not Active).  
    # 0x40000000 For Future Use.  
    # 0x80000000 Channel enabled (1=Enabled, 0=Disabled).  

    # Bits 21 to 28 (Digital Input States) are only applicable if the associated digital input is fitted to your controller - see the relevant handbook for more details. 
    # Tested and working, but output is not in hex

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetStatusBits(serial_number)
    return output

PCC_GetVoltageSource = lib.PCC_GetVoltageSource
PCC_GetVoltageSource.restype = PZ_InputSourceFlags
PCC_GetVoltageSource.argtypes = [POINTER(c_char)]


def get_voltage_source(serial_number):
    # Gets the control voltage source.
    # ReturnsThe voltage source. 
    # Software Only 0  
    # Software and External 1  
    # Software and Potentiometer 2  
    # Software, External and Potentiometer 3  
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetVoltageSource(serial_number)
    return output

PCC_HasLastMsgTimerOverrun = lib.PCC_HasLastMsgTimerOverrun
PCC_HasLastMsgTimerOverrun.restype = c_bool
PCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by PCC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).
    # Returns True if last message timer has elapsed, False if monitoring is not 
    # enabled or if time of last message received is less than lastMsgTimeout.
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_HasLastMsgTimerOverrun(serial_number)

    return output


PCC_Identify = lib.PCC_Identify
PCC_Identify.restype = c_void_p
PCC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    _ = PCC_Identify(serial_number)


PCC_LoadNamedSettings = lib.PCC_LoadNamedSettings
PCC_LoadNamedSettings.restype = c_bool
PCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.
    # Not fully implemented

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    settingsName = POINTER(c_char)

    output = PCC_LoadNamedSettings(serial_number, settingsName)
    return output


PCC_LoadSettings = lib.PCC_LoadSettings
PCC_LoadSettings.restype = c_bool
PCC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.
    # Returns true if successful, false if not

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_LoadSettings(serial_number)

    return output


PCC_MessageQueueSize = lib.PCC_MessageQueueSize
PCC_MessageQueueSize.restype = c_int
PCC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.
    # Returns number of messages in the queue. 
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_MessageQueueSize(serial_number)
    return output

PCC_PersistSettings = lib.PCC_PersistSettings
PCC_PersistSettings.restype = c_bool
PCC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.
    # Returnstrue if successful, false if not. 

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_PersistSettings(serial_number)

    return output


PCC_PollingDuration = lib.PCC_PollingDuration
PCC_PollingDuration.restype = c_long
PCC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.
    # Returns The time between polls in milliseconds or 0 if polling is not active. 
    # Tested and working 08/19/2024
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_PollingDuration(serial_number)
    return output

PCC_RegisterMessageCallback = lib.PCC_RegisterMessageCallback
PCC_RegisterMessageCallback.restype = c_void_p
PCC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.
    # Not implemented

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    void = c_void_p()

    output = PCC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


PCC_RequestFeedbackLoopPIconsts = lib.PCC_RequestFeedbackLoopPIconsts
PCC_RequestFeedbackLoopPIconsts.restype = c_bool
PCC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def request_feedback_loop_pi_consts(serial_number):
    # Requests that the feedback loop constants be read from the device.
    # ReturnsTrue if it succeeds, false if it fails. 
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestFeedbackLoopPIconsts(serial_number)

    return output


PCC_RequestIOSettings = lib.PCC_RequestIOSettings
PCC_RequestIOSettings.restype = c_bool
PCC_RequestIOSettings.argtypes = [POINTER(c_char)]


def request_i_o_settings(serial_number):
    # Requests that the IO settings are read from the device.
    # Returns True if it succeeds, false if it fails
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestIOSettings(serial_number)

    return output


PCC_RequestLEDBrightness = lib.PCC_RequestLEDBrightness
PCC_RequestLEDBrightness.restype = c_bool
PCC_RequestLEDBrightness.argtypes = [POINTER(c_char)]


def request_led_brightness(serial_number):
    # Requests that the LED brightness be read from the device.
    # Returns True if it succeeds, false if it fails. 
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestLEDBrightness(serial_number)

    return output


PCC_RequestPosition = lib.PCC_RequestPosition
PCC_RequestPosition.restype = c_short
PCC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current output voltage or position depending on current mode.
    # Returns None, raises exception upon error
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestPositionControlMode = lib.PCC_RequestPositionControlMode
PCC_RequestPositionControlMode.restype = c_bool
PCC_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    # Requests that the Position Control Mode be read from the device.
    # Returns True if it succeeds, false if it fails.
    # Tested and working 08/19/2024

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestPositionControlMode(serial_number)
    return output

PCC_RequestSettings = lib.PCC_RequestSettings
PCC_RequestSettings.restype = c_short
PCC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.
    # Returns None, raises exception upon error

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestStatus = lib.PCC_RequestStatus
PCC_RequestStatus.restype = c_short
PCC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status and position from the device.
    # This needs to be called to get the device to send it's 
    # current status bits and position.
    # NOTE this is called automatically if Polling is enabled 
    # for the device using PCC_StartPolling(char const * serialNo, int milliseconds). 
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestStatusBits = lib.PCC_RequestStatusBits
PCC_RequestStatusBits.restype = c_short
PCC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.
    # This needs to be called to get the device to send it's current status bits.
    # NOTE this is called automatically if Polling is enabled for the device using 
    # PCC_StartPolling(char const * serialNo, int milliseconds). 
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestVoltageSource = lib.PCC_RequestVoltageSource
PCC_RequestVoltageSource.restype = c_bool
PCC_RequestVoltageSource.argtypes = [POINTER(c_char)]


def request_voltage_source(serial_number):
    # Requests that the current input voltage source be read from the device.
    # Returns True if it succeeds, false if it fails. 
    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestVoltageSource(serial_number)

    return output


PCC_SetFeedbackLoopPIconsts = lib.PCC_SetFeedbackLoopPIconsts
PCC_SetFeedbackLoopPIconsts.restype = c_short
PCC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]


def set_feedback_loop_pi_consts(serial_number, proportionalTerm, integralTerm):
    # Sets the feedback loop constants.
    # Fully Implemented; not tested

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalTerm = c_short(proportionalTerm)
    integralTerm = c_short(integralTerm)

    output = PCC_SetFeedbackLoopPIconsts(serial_number, proportionalTerm, integralTerm)
    if output != 0:
        raise KinesisException(output)


PCC_SetFeedbackLoopPIconstsBlock = lib.PCC_SetFeedbackLoopPIconstsBlock
PCC_SetFeedbackLoopPIconstsBlock.restype = c_short
PCC_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char), PZ_FeedbackLoopConstants]


def set_feedback_loop_pi_consts_block(serial_number):
    # Sets the feedback loop constants in a block.
    # Not implemented

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PCC_SetFeedbackLoopPIconstsBlock(serial_number, proportionalAndIntegralConstants)
    if output != 0:
        raise KinesisException(output)


PCC_SetHubAnalogInput = lib.PCC_SetHubAnalogInput
PCC_SetHubAnalogInput.restype = c_short
PCC_SetHubAnalogInput.argtypes = [POINTER(c_char), HubAnalogueModes]


def set_hub_analog_input(serial_number, hubAnalogueInputMode):
    # Sets the Hub Analog Input.
    # Hub Analogue Input Mode. 
    #   Input applied to all Hub bays 1  
    #   Input applied to adjacent Hub bays 2  
    #   Input is from external SMA 3  

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hubAnalogInput = HubAnalogueModes(hubAnalogueInputMode)

    output = PCC_SetHubAnalogInput(serial_number, hubAnalogInput)
    if output != 0:
        raise KinesisException(output)


PCC_SetIOSettings = lib.PCC_SetIOSettings
PCC_SetIOSettings.restype = c_short
PCC_SetIOSettings.argtypes = [POINTER(c_char), TPZ_IOSettings]


def set_i_o_settings(serial_number):
    # Sets the IO settings.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    ioSettings = TPZ_IOSettings()

    output = PCC_SetIOSettings(serial_number, ioSettings)
    if output != 0:
        raise KinesisException(output)


PCC_SetLEDBrightness = lib.PCC_SetLEDBrightness
PCC_SetLEDBrightness.restype = c_short
PCC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_led_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    brightness = c_short()

    output = PCC_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


PCC_SetLUTwaveParams = lib.PCC_SetLUTwaveParams
PCC_SetLUTwaveParams.restype = c_short
PCC_SetLUTwaveParams.argtypes = [POINTER(c_char), PZ_LUTWaveParameters]


def set_l_u_twave_params(serial_number):
    # Sets the LUT output wave parameters.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    LUTwaveParams = PZ_LUTWaveParameters()

    output = PCC_SetLUTwaveParams(serial_number, LUTwaveParams)
    if output != 0:
        raise KinesisException(output)


PCC_SetLUTwaveSample = lib.PCC_SetLUTwaveSample
PCC_SetLUTwaveSample.restype = c_short
PCC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_long]


def set_l_u_twave_sample(serial_number):
    # Sets a waveform sample.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    index = c_short()
    value = c_long()

    output = PCC_SetLUTwaveSample(serial_number, index, value)
    if output != 0:
        raise KinesisException(output)


PCC_SetPosition = lib.PCC_SetPosition
PCC_SetPosition.restype = c_short
PCC_SetPosition.argtypes = [POINTER(c_char), c_long]


def set_position(serial_number):
    # Sets the position when in closed loop mode.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_long()

    output = PCC_SetPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


PCC_SetPositionControlMode = lib.PCC_SetPositionControlMode
PCC_SetPositionControlMode.restype = c_short
PCC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]


def set_position_control_mode(serial_number):
    # Sets the Position Control Mode.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = PZ_ControlModeTypes()

    output = PCC_SetPositionControlMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


PCC_SetPositionToTolerance = lib.PCC_SetPositionToTolerance
PCC_SetPositionToTolerance.restype = c_short
PCC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_long, c_long]


def set_position_to_tolerance(serial_number):
    # Sets the position when in closed loop mode.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_long()
    tolerance = c_long()

    output = PCC_SetPositionToTolerance(serial_number, position, tolerance)
    if output != 0:
        raise KinesisException(output)


PCC_SetVoltageSource = lib.PCC_SetVoltageSource
PCC_SetVoltageSource.restype = c_short
PCC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]


def set_voltage_source(serial_number):
    # Sets the control voltage source.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    source = PZ_InputSourceFlags()

    output = PCC_SetVoltageSource(serial_number, source)
    if output != 0:
        raise KinesisException(output)


PCC_SetZero = lib.PCC_SetZero
PCC_SetZero.restype = c_bool
PCC_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    # Set zero reference voltage.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_SetZero(serial_number)

    return output


PCC_StartLUTwave = lib.PCC_StartLUTwave
PCC_StartLUTwave.restype = c_short
PCC_StartLUTwave.argtypes = [POINTER(c_char)]


def start_l_u_twave(serial_number):
    # Starts the LUT waveform output.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_StartLUTwave(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_StartPolling = lib.PCC_StartPolling
PCC_StartPolling.restype = c_bool
PCC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    milliseconds = c_int()

    output = PCC_StartPolling(serial_number, milliseconds)

    return output


PCC_StopLUTwave = lib.PCC_StopLUTwave
PCC_StopLUTwave.restype = c_short
PCC_StopLUTwave.argtypes = [POINTER(c_char)]


def stop_l_u_twave(serial_number):
    # Stops the LUT waveform output.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_StopLUTwave(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_StopPolling = lib.PCC_StopPolling
PCC_StopPolling.restype = c_void_p
PCC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_TimeSinceLastMsgReceived = lib.PCC_TimeSinceLastMsgReceived
PCC_TimeSinceLastMsgReceived.restype = c_bool
PCC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lastUpdateTimeMS = c_int64()

    output = PCC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


PCC_WaitForMessage = lib.PCC_WaitForMessage
PCC_WaitForMessage.restype = c_bool
PCC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PCC_WaitForMessage(serial_number, messageType, messageID, messageData)

    return output


TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [c_void_p]


def build_device_list():
    # Build the DeviceList.

    output = TLI_BuildDeviceList(c_void_p())

    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]


def get_device_info(serial_number):
    # Get the device information from the USB port.

    serial_number = POINTER[c_char]
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

    return output


TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p


def initialize_simulations():
    # Initialize a connection to the Simulation Manager, which must already be running.

    output = TLI_InitializeSimulations()
    if output != 0:
        raise KinesisException(output)
