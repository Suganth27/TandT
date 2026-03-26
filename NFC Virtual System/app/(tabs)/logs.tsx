import { View, Text, FlatList } from 'react-native';
import useLogs from '../../hooks/useLogs';

export default function Logs() {
  const { logs } = useLogs();

  return (
    <View style={{
      flex: 1,
      backgroundColor: "#0F172A",
      paddingHorizontal: 20,
      paddingTop: 50
    }}>
      
      <Text style={{
        color: "white",
        fontSize: 24,
        fontWeight: "700",
        marginBottom: 20
      }}>
        Activity Logs
      </Text>

      <FlatList
        data={logs}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <View style={{
            backgroundColor: "#1E293B",
            padding: 18,
            borderRadius: 16,
            marginBottom: 12,
            borderLeftWidth: 4,
            borderLeftColor: item.status.includes("Granted")
              ? "#22C55E"
              : "#EF4444"
          }}>
            <Text style={{ color: "white", fontWeight: "600" }}>
              {item.status}
            </Text>
            <Text style={{ color: "#94A3B8", marginTop: 6 }}>
              {item.time}
            </Text>
          </View>
        )}
      />
    </View>
  );
}