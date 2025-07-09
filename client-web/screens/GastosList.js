import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';

const gastos = [
  { id: '1', nombre: 'Comida', monto: 120 },
  { id: '2', nombre: 'Transporte', monto: 50 }
];

export default function GastosList() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Lista de Gastos</Text>
      <FlatList
        data={gastos}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Text style={styles.item}>{item.nombre}: ${item.monto}</Text>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', padding: 20 },
  title: { color: '#FFD700', fontSize: 24, marginBottom: 20, textAlign: 'center' },
  item: { color: '#fff', padding: 10, backgroundColor: '#2E0854', marginBottom: 5, borderRadius: 5 }
});