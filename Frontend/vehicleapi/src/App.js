import React, { useEffect, useState } from 'react';
import './App.css';
import Vehicles from './components/Vehicles';
import VehicleLoadingComponent from './components/VehicleLoading';

function App() {
	const VehicleLoading = VehicleLoadingComponent(Vehicles);
	const [appState, setAppState] = useState({
		loading: false,
		vehicles: null,
	});

	useEffect(() => {
		setAppState({ loading: true });
		const apiUrl = `http://127.0.0.1:8000/api/`;
		fetch(apiUrl)
			.then((data) => data.json())
			.then((vehicles) => {
				setAppState({ loading: false, vehicles: vehicles });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest Vehicles</h1>
			<VehicleLoading isLoading={appState.loading} vehicles={appState.vehicles} />
		</div>
	);
}
export default App;