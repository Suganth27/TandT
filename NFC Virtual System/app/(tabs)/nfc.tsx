// import { View, Text, Pressable, Animated } from 'react-native';
// import { useRef, useState } from 'react';
// import useLogs from '../../hooks/useLogs';

// export default function NFC() {
//   const scale = useRef(new Animated.Value(1)).current;
//   const [scanning, setScanning] = useState(false);
//   const [success, setSuccess] = useState(false);
//   const { addLog } = useLogs();

//   const startScan = () => {
//     setScanning(true);
//     setSuccess(false);
//     addLog("NFC Scan Started");

//     // Pulse animation
//     Animated.loop(
//       Animated.sequence([
//         Animated.timing(scale, { toValue: 1.2, duration: 500, useNativeDriver: true }),
//         Animated.timing(scale, { toValue: 1, duration: 500, useNativeDriver: true }),
//       ])
//     ).start();

//     setTimeout(() => {
//       setScanning(false);
//       setSuccess(true);
//       addLog("NFC Access Granted");

//       Animated.timing(scale, {
//         toValue: 1,
//         duration: 200,
//         useNativeDriver: true,
//       }).start();
//     }, 2000);
//   };

//   return (
//     <View style={{
//       flex: 1,
//       backgroundColor: "#0F172A",
//       justifyContent: "center",
//       alignItems: "center",
//       paddingHorizontal: 20
//     }}>

//       {/* TITLE */}
//       <Text style={{
//         color: "white",
//         fontSize: 22,
//         fontWeight: "600",
//         marginBottom: 20
//       }}>
//         NFC Access
//       </Text>

//       {/* ANIMATED CIRCLE */}
//       <Animated.View style={{
//         width: 120,
//         height: 120,
//         borderRadius: 60,
//         backgroundColor: success ? "#22C55E" : "#4F46E5",
//         justifyContent: "center",
//         alignItems: "center",
//         transform: [{ scale }]
//       }}>
//         <Text style={{ color: "white", fontWeight: "600" }}>
//           {success ? "✓" : "NFC"}
//         </Text>
//       </Animated.View>

//       {/* STATUS TEXT */}
//       <Text style={{
//         color: "white",
//         marginTop: 20,
//         fontSize: 16
//       }}>
//         {success
//           ? "Access Granted"
//           : scanning
//           ? "Scanning..."
//           : "Tap to Scan"}
//       </Text>

//       {/* BUTTON */}
//       {!scanning && (
//         <Pressable
//           onPress={startScan}
//           style={{
//             marginTop: 20,
//             backgroundColor: "#4F46E5",
//             padding: 14,
//             borderRadius: 12
//           }}
//         >
//           <Text style={{ color: "white" }}>
//             Start NFC Scan
//           </Text>
//         </Pressable>
//       )}

//     </View>
//   );
// }
import { View, Text, Pressable, Animated } from 'react-native';
import { useRef, useState } from 'react';
import useLogs from '../../hooks/useLogs';

export default function NFC() {
  const scale = useRef(new Animated.Value(1)).current;
  const animationRef = useRef<any>(null); // control animation
  const [scanning, setScanning] = useState(false);
  const [status, setStatus] = useState("Tap to Scan");
  const { addLog } = useLogs();

  const startScan = () => {
    setScanning(true);
    setStatus("Scanning...");
    addLog("NFC Scan Started");

    // Start animation
    animationRef.current = Animated.loop(
      Animated.sequence([
        Animated.timing(scale, { toValue: 1.2, duration: 500, useNativeDriver: true }),
        Animated.timing(scale, { toValue: 1, duration: 500, useNativeDriver: true }),
      ])
    );

    animationRef.current.start();

    // Run scan for few seconds
    setTimeout(() => {
      setStatus("No device detected");
      addLog("No NFC device found");

      // Stop animation
      animationRef.current.stop();
      scale.setValue(1);

      // Allow user to scan again
      setScanning(false);

    }, 3000);
  };

  return (
    <View style={{
      flex: 1,
      backgroundColor: "#0F172A",
      justifyContent: "center",
      alignItems: "center",
      paddingHorizontal: 20
    }}>

      {/* TITLE */}
      <Text style={{
        color: "white",
        fontSize: 22,
        fontWeight: "600",
        marginBottom: 20
      }}>
        NFC Access
      </Text>

      {/* ANIMATED CIRCLE */}
      <Animated.View style={{
        width: 120,
        height: 120,
        borderRadius: 60,
        backgroundColor: "#4F46E5",
        justifyContent: "center",
        alignItems: "center",
        transform: [{ scale }]
      }}>
        <Text style={{ color: "white", fontWeight: "600" }}>
          NFC
        </Text>
      </Animated.View>

      {/* STATUS TEXT */}
      <Text style={{
        color: "white",
        marginTop: 20,
        fontSize: 16
      }}>
        {status}
      </Text>

      {/* BUTTON */}
      {!scanning && (
        <Pressable
          onPress={startScan}
          style={{
            marginTop: 20,
            backgroundColor: "#4F46E5",
            padding: 14,
            borderRadius: 12
          }}
        >
          <Text style={{ color: "white" }}>
            Start NFC Scan
          </Text>
        </Pressable>
      )}

    </View>
  );
}