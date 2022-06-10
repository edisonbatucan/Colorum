import React, { useEffect, useState } from "react";
import './App.css'
import Vehicle from './components/Vehicle';
import VehicleLoadingComponent from './components/VehicleLoading';

function App() {
	const VehicleLoading = VehicleLoadingComponent(Vehicle);
	const [appState, setAppState] = useState({
		loading: false,
		vehicle: null,
	});

	useEffect(() => {
		setAppState({ loading: true });
		const apiUrl = `http://127.0.0.1:8000/api/a`;
		fetch(apiUrl)
			.then((data) => data.json())
			.then((vehicle) => {
				setAppState({ loading: false, vehicle: vehicle });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest Vehicle</h1>
			<VehicleLoading isLoading={appState.loading} vehicle={appState.vehicle} />
		</div>
	);
}
export default App;