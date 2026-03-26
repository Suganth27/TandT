import { View, Text, TextInput, Pressable } from 'react-native';
import { useState } from 'react';
import { useRouter } from 'expo-router';

export default function Login() {
  const [pin, setPin] = useState('');
  const router = useRouter();

  return (
    <View style={{
      flex: 1,
      backgroundColor: "#0F172A",
      paddingHorizontal: 24,
      justifyContent: "center"
    }}>
      
      <Text style={{
        color: "white",
        fontSize: 34,
        fontWeight: "bold",
        marginBottom: 8
      }}>
        Tap & Trust
      </Text>

      <Text style={{
        color: "#94A3B8",
        marginBottom: 40
      }}>
        Secure access made simple
      </Text>

      <TextInput
        placeholder="Enter PIN"
        placeholderTextColor="#64748B"
        secureTextEntry
        keyboardType="numeric"
        onChangeText={setPin}
        style={{
          backgroundColor: "#1E293B",
          padding: 18,
          borderRadius: 14,
          color: "white",
          fontSize: 16,
          marginBottom: 20
        }}
      />

      <Pressable
        onPress={() => {
          if (pin === "1234") {
            router.replace('/home');
          }
        }}
        style={{
          backgroundColor: "#4F46E5",
          padding: 18,
          borderRadius: 14,
          alignItems: "center",
          shadowColor: "#4F46E5",
          shadowOpacity: 0.4,
          shadowRadius: 10
        }}
      >
        <Text style={{
          color: "white",
          fontSize: 16,
          fontWeight: "600"
        }}>
          Unlock Access
        </Text>
      </Pressable>

    </View>
  );
}