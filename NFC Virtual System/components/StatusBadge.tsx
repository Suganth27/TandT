import { Text } from 'react-native';
import Colors from '../constants/Colors';

export default function StatusBadge({ status }: any) {
  const color =
    status === "Connected" ? Colors.success : Colors.danger;

  return (
    <Text style={{ color, fontWeight: "bold" }}>
      {status}
    </Text>
  );
}