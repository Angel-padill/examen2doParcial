import React from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

export default function RegisterGasto() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Registrar Gasto</Text>
      <TextInput style={styles.input} placeholder="Nombre del gasto" placeholderTextColor="#ccc" />
      <TextInput style={styles.input} placeholder="Monto" placeholderTextColor="#ccc" keyboardType="numeric" />
      <Button title="Guardar" color="#FFD700" onPress={() => {}} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', padding: 20, justifyContent: 'center' },
  title: { color: '#FFD700', fontSize: 24, marginBottom: 20, textAlign: 'center' },
  input: { backgroundColor: '#2E0854', color: '#fff', padding: 10, marginBottom: 10, borderRadius: 5 }
});