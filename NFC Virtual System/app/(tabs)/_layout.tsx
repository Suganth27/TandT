import { Tabs } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function TabsLayout() {
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarStyle: { backgroundColor: "#0F172A" },
        tabBarActiveTintColor: "#4F46E5",
        tabBarInactiveTintColor: "gray"
      }}
    >
      <Tabs.Screen name="home" options={{
        title: "Home",
        tabBarIcon: ({ color }) => <Ionicons name="home" size={20} color={color} />
      }} />

      <Tabs.Screen name="device" options={{
        title: "Device",
        tabBarIcon: ({ color }) => <Ionicons name="bluetooth" size={20} color={color} />
      }} />

      <Tabs.Screen name="nfc" options={{
        title: "NFC",
        tabBarIcon: ({ color }) => <Ionicons name="scan" size={20} color={color} />
      }} />

      <Tabs.Screen name="logs" options={{
        title: "Logs",
        tabBarIcon: ({ color }) => <Ionicons name="list" size={20} color={color} />
      }} />

      <Tabs.Screen name="settings" options={{
        title: "Settings",
        tabBarIcon: ({ color }) => <Ionicons name="settings" size={20} color={color} />
      }} />
    </Tabs>
  );
}