import { View, Text, Pressable, FlatList, Animated } from 'react-native';
import usePressAnimation from '../../hooks/usePressAnimation';
import useLogs from '../../hooks/useLogs';

export default function Home() {
  const { scale, onPressIn, onPressOut } = usePressAnimation();
  const { logs, addLog } = useLogs();

  return (
    <View style={{
      flex: 1,
      backgroundColor: "#0F172A",
      paddingHorizontal: 20,
      paddingTop: 50
    }}>

      {/* 🔹 HEADER */}
      <Text style={{
        color: "white",
        fontSize: 26,
        fontWeight: "700"
      }}>
        Dashboard
      </Text>

      <Text style={{
        color: "#94A3B8",
        marginTop: 4,
        marginBottom: 25
      }}>
        Welcome back 👋
      </Text>

      {/* 🔹 STATUS CARD */}
      <View style={{
        backgroundColor: "#1E293B",
        padding: 18,
        borderRadius: 18,
        marginBottom: 20
      }}>
        <Text style={{ color: "#94A3B8", fontSize: 13 }}>
          Device Status
        </Text>

        <Text style={{
          color: "#22C55E",
          fontSize: 18,
          fontWeight: "600",
          marginTop: 6
        }}>
          Connected ✅
        </Text>
      </View>

      {/* 🔹 QUICK ACTIONS */}
      <Text style={{
        color: "white",
        fontSize: 18,
        fontWeight: "600",
        marginBottom: 10
      }}>
        Quick Actions
      </Text>

      <View style={{
        flexDirection: "row",
        justifyContent: "space-between",
        marginBottom: 20
      }}>

        {/* Unlock */}
        <Animated.View style={{ transform: [{ scale }], flex: 1, marginRight: 10 }}>
          <Pressable
            onPressIn={onPressIn}
            onPressOut={onPressOut}
            onPress={() => addLog("Access Granted")}
            style={{
              backgroundColor: "#4F46E5",
              padding: 18,
              borderRadius: 16,
              alignItems: "center"
            }}
          >
            <Text style={{ color: "white", fontWeight: "600" }}>
              Unlock
            </Text>
          </Pressable>
        </Animated.View>

        {/* Scan */}
        <Animated.View style={{ transform: [{ scale }], flex: 1, marginLeft: 10 }}>
          <Pressable
            onPressIn={onPressIn}
            onPressOut={onPressOut}
            onPress={() => addLog("Scan Triggered")}
            style={{
              backgroundColor: "#334155",
              padding: 18,
              borderRadius: 16,
              alignItems: "center"
            }}
          >
            <Text style={{ color: "white", fontWeight: "600" }}>
              Scan
            </Text>
          </Pressable>
        </Animated.View>

      </View>

      {/* 🔹 RECENT ACTIVITY */}
      <Text style={{
        color: "white",
        fontSize: 18,
        fontWeight: "600",
        marginBottom: 10
      }}>
        Recent Activity
      </Text>

      <FlatList
        data={logs.slice(0, 3)} // show only latest 3
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{
            backgroundColor: "#1E293B",
            padding: 16,
            borderRadius: 14,
            marginBottom: 10,
            borderLeftWidth: 4,
            borderLeftColor: item.status.includes("Granted")
              ? "#22C55E"
              : "#EF4444"
          }}>
            <Text style={{ color: "white", fontWeight: "600" }}>
              {item.status}
            </Text>
            <Text style={{
              color: "#94A3B8",
              marginTop: 4,
              fontSize: 12
            }}>
              {item.time}
            </Text>
          </View>
        )}
      />

    </View>
  );
}