import { View } from 'react-native';
import Colors from '../constants/Colors';

export default function Card({ children }: any) {
  return (
    <View
      style={{
        backgroundColor: Colors.card,
        padding: 15,
        borderRadius: 12,
        marginVertical: 10,
      }}
    >
      {children}
    </View>
  );
}