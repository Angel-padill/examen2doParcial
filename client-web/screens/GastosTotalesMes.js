import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function GastosTotalesMes() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Total del Mes</Text>
      <Text style={styles.total}>$170</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000', justifyContent: 'center', alignItems: 'center' },
  title: { color: '#FFD700', fontSize: 24, marginBottom: 20 },
  total: { color: '#fff', fontSize: 40 }
});