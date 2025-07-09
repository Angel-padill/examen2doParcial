import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';

import RegisterGasto from './screens/RegisterGasto';
import GastosList from './screens/GastosList';
import GastosTotalesMes from './screens/GastosTotalesMes';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <StatusBar style="light" />
      <Stack.Navigator initialRouteName="Registrar Gasto"
        screenOptions={{
          headerStyle: { backgroundColor: '#2E0854' },
          headerTintColor: '#FFD700',
          headerTitleStyle: { fontWeight: 'bold' }
        }}>
        <Stack.Screen name="Registrar Gasto" component={RegisterGasto} />
        <Stack.Screen name="Lista de Gastos" component={GastosList} />
        <Stack.Screen name="Total del Mes" component={GastosTotalesMes} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}