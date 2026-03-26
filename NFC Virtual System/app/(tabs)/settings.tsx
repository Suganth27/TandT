import { View, Text, Pressable } from 'react-native';
import { useRouter } from 'expo-router';
import usePressAnimation from '../../hooks/usePressAnimation';
import { Animated } from 'react-native';

export default function Settings() {
  const router = useRouter();
  const { scale, onPressIn, onPressOut } = usePressAnimation();

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
        marginBottom: 20
      }}>
        Settings
      </Text>

      {/* PROFILE CARD */}
      <View style={{
        backgroundColor: "#1E293B",
        padding: 18,
        borderRadius: 16,
        marginBottom: 20
      }}>
        <Text style={{ color: "#94A3B8" }}>User</Text>
        <Text style={{
          color: "white",
          marginTop: 6,
          fontSize: 16,
          fontWeight: "600"
        }}>
          Admin
        </Text>
      </View>

      {/* APP INFO */}
      <View style={{
        backgroundColor: "#1E293B",
        padding: 18,
        borderRadius: 16,
        marginBottom: 20
      }}>
        <Text style={{ color: "#94A3B8" }}>App Version</Text>
        <Text style={{ color: "white", marginTop: 6 }}>
          v1.0.0
        </Text>

        <Text style={{
          color: "#94A3B8",
          marginTop: 10
        }}>
          Last Sync
        </Text>

        <Text style={{ color: "white", marginTop: 4 }}>
          Just now
        </Text>
      </View>

      {/* LOGOUT BUTTON */}
      <Animated.View style={{ transform: [{ scale }] }}>
        <Pressable
          onPressIn={onPressIn}
          onPressOut={onPressOut}
          onPress={() => router.replace('/login')}
          style={{
            backgroundColor: "#EF4444",
            padding: 16,
            borderRadius: 14,
            alignItems: "center"
          }}
        >
          <Text style={{
            color: "white",
            fontWeight: "600"
          }}>
            Logout
          </Text>
        </Pressable>
      </Animated.View>

    </View>
  );
}