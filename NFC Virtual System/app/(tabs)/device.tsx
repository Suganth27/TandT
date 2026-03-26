import { View, Text, FlatList, Pressable, Animated } from 'react-native';
import { useState } from 'react';
import usePressAnimation from '../../hooks/usePressAnimation';
import useLogs from '../../hooks/useLogs';

export default function Device() {
  const [devices, setDevices] = useState<any[]>([]);
  const [scanning, setScanning] = useState(false);

  const { scale, onPressIn, onPressOut } = usePressAnimation();
  const { addLog } = useLogs();

  // 🔍 Scan Devices (Mock)
  const scanDevices = () => {
    setDevices([]);
    setScanning(true);
    addLog("Scanning for BLE devices...");

    setTimeout(() => {
      const foundDevices = [
        { id: "1", name: "ESP32 Smart Lock", rssi: "-52 dBm", status: "Nearby" },
        { id: "2", name: "Office Sensor", rssi: "-68 dBm", status: "Nearby" },
        { id: "3", name: "Door Controller", rssi: "-60 dBm", status: "Nearby" }
      ];

      setDevices(foundDevices);
      setScanning(false);
      addLog("Devices discovered successfully");
    }, 2000);
  };

  // 🔌 Connect Device
  const connectDevice = (id: string) => {
    setDevices(prev =>
      prev.map(d =>
        d.id === id ? { ...d, status: "Connecting..." } : d
      )
    );

    const device = devices.find(d => d.id === id);
    addLog(`Connecting to ${device?.name}...`);

    setTimeout(() => {
      setDevices(prev =>
        prev.map(d =>
          d.id === id ? { ...d, status: "Connected" } : d
        )
      );

      addLog(`${device?.name} connected successfully`);
    }, 1500);
  };

  return (
    <View style={{
      flex: 1,
      backgroundColor: "#0F172A",
      paddingHorizontal: 20,
      paddingTop: 50
    }}>

      {/* HEADER */}
      <Text style={{
        color: "white",
        fontSize: 24,
        fontWeight: "700",
        marginBottom: 5
      }}>
        Devices
      </Text>

      <Text style={{
        color: "#94A3B8",
        marginBottom: 20
      }}>
        Manage and connect devices
      </Text>

      {/* 🔍 SCAN BUTTON */}
      <Animated.View style={{ transform: [{ scale }] }}>
        <Pressable
          onPressIn={onPressIn}
          onPressOut={onPressOut}
          onPress={scanDevices}
          style={{
            backgroundColor: "#4F46E5",
            padding: 16,
            borderRadius: 14,
            alignItems: "center",
            marginBottom: 20
          }}
        >
          <Text style={{ color: "white", fontWeight: "600" }}>
            {scanning ? "Scanning..." : "Scan BLE Devices"}
          </Text>
        </Pressable>
      </Animated.View>

      {/* STATUS TEXT */}
      {scanning && (
        <Text style={{
          color: "#94A3B8",
          marginBottom: 10
        }}>
          Searching nearby devices...
        </Text>
      )}

      {/* 📡 DEVICE LIST */}
      <FlatList
        data={devices}
        keyExtractor={(item) => item.id}
        showsVerticalScrollIndicator={false}
        contentContainerStyle={{ paddingBottom: 20 }}
        renderItem={({ item }) => (
          <View style={{
            backgroundColor: "#1E293B",
            padding: 18,
            borderRadius: 16,
            marginBottom: 12
          }}>
            
            {/* NAME */}
            <Text style={{
              color: "white",
              fontSize: 16,
              fontWeight: "600"
            }}>
              {item.name}
            </Text>

            {/* SIGNAL */}
            <Text style={{
              color: "#94A3B8",
              marginTop: 6
            }}>
              Signal: {item.rssi}
            </Text>

            {/* STATUS */}
            <Text style={{
              marginTop: 6,
              color:
                item.status === "Connected"
                  ? "#22C55E"
                  : item.status === "Connecting..."
                  ? "#FACC15"
                  : "#94A3B8",
              fontWeight: "600"
            }}>
              {item.status}
            </Text>

            {/* CONNECT BUTTON */}
            {item.status !== "Connected" && (
              <Pressable
                onPress={() => connectDevice(item.id)}
                style={{
                  marginTop: 12,
                  backgroundColor: "#4F46E5",
                  padding: 12,
                  borderRadius: 12,
                  alignItems: "center"
                }}
              >
                <Text style={{
                  color: "white",
                  fontWeight: "600"
                }}>
                  {item.status === "Connecting..." ? "Connecting..." : "Connect"}
                </Text>
              </Pressable>
            )}

          </View>
        )}
      />
    </View>
  );
}