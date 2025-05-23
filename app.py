import streamlit as st
import pickle
import pandas as pd

def predict_using_file(file_name):
    model = pickle.load(open('model.pkl', 'rb'))
    file_name = "sample_inputs//"+file_name
    with open(file_name, 'r') as f:
        x = f.read()
        random_sample = {}
        for line in x.split('\n'):
            if line:
                key, value = line.split()
                random_sample[key] = int(float(value))
        random_sample = pd.DataFrame(random_sample, index=[0])
        random_sample_pred = model.predict(random_sample)
        return "Suspicious Activity Detected! Potential Rootkit Found!" if random_sample_pred[0] == 1 else "No Rootkit Detected!"
    
    
def predict_using_input(random_sample):
    model = pickle.load(open('model.pkl', 'rb'))
    random_sample = pd.DataFrame(random_sample, index=[0])
    random_sample_pred = model.predict(random_sample)
    return "Suspicious Activity Detected! Potential Rootkit Found!" if random_sample_pred[0] == 1 else "No Rootkit Detected!"

        
        
def main():
    st.title("Rootkit Detection")
    option = st.selectbox('Select an option:', ['__select__', 'Upload a file', 'Enter the values'])
    if option == 'Upload a file':
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            file = uploaded_file.name
            if st.button('Detect the presence of Rootkit'):
                result = predict_using_file(file)
                if result == "Suspicious Activity Detected! Potential Rootkit Found!":
                    st.error(result)
                else:
                    st.success(result)
    elif option == 'Enter the values':

        all_values = ['transact', 'onServiceConnected', 'bindService', 'attachInterface', 'ServiceConnection', 'android.os.Binder', 'SEND_SMS', 'Ljava.lang.Class.getCanonicalName', 'Ljava.lang.Class.getMethods', 'Ljava.lang.Class.cast', 'Ljava.net.URLDecoder', 'android.content.pm.Signature', 'android.telephony.SmsManager', 'READ_PHONE_STATE', 'getBinder', 'ClassLoader', 'Landroid.content.Context.registerReceiver', 'Ljava.lang.Class.getField', 'Landroid.content.Context.unregisterReceiver', 'GET_ACCOUNTS', 'RECEIVE_SMS', 'Ljava.lang.Class.getDeclaredField', 'READ_SMS', 'getCallingUid', 'Ljavax.crypto.spec.SecretKeySpec', 'android.intent.action.BOOT_COMPLETED', 'USE_CREDENTIALS', 'MANAGE_ACCOUNTS', 'android.content.pm.PackageInfo', 'KeySpec', 'TelephonyManager.getLine1Number', 'DexClassLoader', 'HttpGet.init', 'SecretKey', 'Ljava.lang.Class.getMethod', 'System.loadLibrary', 'android.intent.action.SEND', 'Ljavax.crypto.Cipher', 'WRITE_SMS', 'READ_SYNC_SETTINGS', 'AUTHENTICATE_ACCOUNTS', 'android.telephony.gsm.SmsManager', 'WRITE_HISTORY_BOOKMARKS', 'TelephonyManager.getSubscriberId', 'mount', 'INSTALL_PACKAGES', 'Runtime.getRuntime', 'CAMERA', 'Ljava.lang.Object.getClass', 'WRITE_SYNC_SETTINGS', 'READ_HISTORY_BOOKMARKS', 'Ljava.lang.Class.forName', 'INTERNET', 'android.intent.action.PACKAGE_REPLACED', 'Binder', 'android.intent.action.SEND_MULTIPLE', 'RECORD_AUDIO', 'IBinder', 'android.os.IBinder', 'createSubprocess', 'NFC', 'ACCESS_LOCATION_EXTRA_COMMANDS', 'URLClassLoader', 'WRITE_APN_SETTINGS', 'abortBroadcast', 'BIND_REMOTEVIEWS', 'android.intent.action.TIME_SET', 'READ_PROFILE', 'TelephonyManager.getDeviceId', 'MODIFY_AUDIO_SETTINGS', 'getCallingPid', 'READ_SYNC_STATS', 'BROADCAST_STICKY', 'android.intent.action.PACKAGE_REMOVED', 'android.intent.action.TIMEZONE_CHANGED', 'WAKE_LOCK', 'RECEIVE_BOOT_COMPLETED', 'RESTART_PACKAGES', 'Ljava.lang.Class.getPackage', 'chmod', 'Ljava.lang.Class.getDeclaredClasses', 'android.intent.action.ACTION_POWER_DISCONNECTED', 'android.intent.action.PACKAGE_ADDED', 'PathClassLoader', 'TelephonyManager.getSimSerialNumber', 'Runtime.load', 'TelephonyManager.getCallState', 'BLUETOOTH', 'READ_CALENDAR', 'READ_CALL_LOG', 'SUBSCRIBED_FEEDS_WRITE', 'READ_EXTERNAL_STORAGE', 'TelephonyManager.getSimCountryIso', 'sendMultipartTextMessage', 'PackageInstaller', 'VIBRATE', 'remount', 'android.intent.action.ACTION_SHUTDOWN', 'sendDataMessage', 'ACCESS_NETWORK_STATE', 'chown', 'HttpPost.init', 'Ljava.lang.Class.getClasses', 'SUBSCRIBED_FEEDS_READ', 'TelephonyManager.isNetworkRoaming', 'CHANGE_WIFI_MULTICAST_STATE', 'WRITE_CALENDAR', 'android.intent.action.PACKAGE_DATA_CLEARED', 'MASTER_CLEAR', 'HttpUriRequest', 'UPDATE_DEVICE_STATS', 'WRITE_CALL_LOG', 'DELETE_PACKAGES', 'GET_TASKS', 'GLOBAL_SEARCH', 'DELETE_CACHE_FILES', 'WRITE_USER_DICTIONARY', 'android.intent.action.PACKAGE_CHANGED', 'android.intent.action.NEW_OUTGOING_CALL', 'REORDER_TASKS', 'WRITE_PROFILE', 'SET_WALLPAPER', 'BIND_INPUT_METHOD', 'divideMessage', 'READ_SOCIAL_STREAM', 'READ_USER_DICTIONARY', 'PROCESS_OUTGOING_CALLS', 'CALL_PRIVILEGED', 'Runtime.exec', 'BIND_WALLPAPER', 'RECEIVE_WAP_PUSH', 'DUMP', 'BATTERY_STATS', 'ACCESS_COARSE_LOCATION', 'SET_TIME', 'android.intent.action.SENDTO', 'WRITE_SOCIAL_STREAM', 'WRITE_SETTINGS', 'REBOOT', 'BLUETOOTH_ADMIN', 'TelephonyManager.getNetworkOperator', '/system/bin', 'MessengerService', 'BIND_DEVICE_ADMIN', 'WRITE_GSERVICES', 'IRemoteService', 'KILL_BACKGROUND_PROCESSES', 'SET_ALARM', 'ACCOUNT_MANAGER', '/system/app', 'android.intent.action.CALL', 'STATUS_BAR', 'TelephonyManager.getSimOperator', 'PERSISTENT_ACTIVITY', 'CHANGE_NETWORK_STATE', 'onBind', 'Process.start', 'android.intent.action.SCREEN_ON', 'Context.bindService', 'RECEIVE_MMS', 'SET_TIME_ZONE', 'android.intent.action.BATTERY_OKAY', 'CONTROL_LOCATION_UPDATES', 'BROADCAST_WAP_PUSH', 'BIND_ACCESSIBILITY_SERVICE', 'ADD_VOICEMAIL', 'CALL_PHONE', 'ProcessBuilder', 'BIND_APPWIDGET', 'FLASHLIGHT', 'READ_LOGS', 'Ljava.lang.Class.getResource', 'defineClass', 'SET_PROCESS_LIMIT', 'android.intent.action.PACKAGE_RESTARTED', 'MOUNT_UNMOUNT_FILESYSTEMS', 'BIND_TEXT_SERVICE', 'INSTALL_LOCATION_PROVIDER', 'android.intent.action.CALL_BUTTON', 'android.intent.action.SCREEN_OFF', 'findClass', 'SYSTEM_ALERT_WINDOW', 'MOUNT_FORMAT_FILESYSTEMS', 'CHANGE_CONFIGURATION', 'CLEAR_APP_USER_DATA', 'intent.action.RUN', 'android.intent.action.SET_WALLPAPER', 'CHANGE_WIFI_STATE', 'READ_FRAME_BUFFER', 'ACCESS_SURFACE_FLINGER', 'Runtime.loadLibrary', 'BROADCAST_SMS', 'EXPAND_STATUS_BAR', 'INTERNAL_SYSTEM_WINDOW', 'android.intent.action.BATTERY_LOW', 'SET_ACTIVITY_WATCHER', 'WRITE_CONTACTS', 'android.intent.action.ACTION_POWER_CONNECTED', 'BIND_VPN_SERVICE', 'DISABLE_KEYGUARD', 'ACCESS_MOCK_LOCATION', 'GET_PACKAGE_SIZE', 'MODIFY_PHONE_STATE', 'CHANGE_COMPONENT_ENABLED_STATE', 'CLEAR_APP_CACHE', 'SET_ORIENTATION', 'READ_CONTACTS', 'DEVICE_POWER', 'HARDWARE_TEST', 'ACCESS_WIFI_STATE', 'WRITE_EXTERNAL_STORAGE', 'ACCESS_FINE_LOCATION', 'SET_WALLPAPER_HINTS', 'SET_PREFERRED_APPLICATIONS', 'WRITE_SECURE_SETTINGS']
        
        values = st.multiselect('Select the values:', all_values)
        
        
        dataframe = {}
        for value in all_values:
            if value in values:
                dataframe[value] = 1.0
            else:
                dataframe[value] = 0.0
        if st.button('Detect the presence of Rootkit'):
            result = predict_using_input(dataframe)
            if result == "Suspicious Activity Detected! Potential Rootkit Found!":
                st.error(result)
            else:
                st.success(result)


if __name__ == '__main__':
    main()