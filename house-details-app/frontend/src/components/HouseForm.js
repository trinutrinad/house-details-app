import React, { useState } from 'react';

const HouseForm = () => {
    const [ownerName, setOwnerName] = useState('');
    const [aadharNumber, setAadharNumber] = useState('');
    const [length, setLength] = useState('');
    const [breadth, setBreadth] = useState('');
    const [roofType, setRoofType] = useState('');
    const [yearOfConstruction, setYearOfConstruction] = useState('');
    const [drainageType, setDrainageType] = useState('');
    const [roadType, setRoadType] = useState('');
    const [electricityConnectionType, setElectricityConnectionType] = useState('');
    const [houseType, setHouseType] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        const houseDetails = {
            ownerName,
            aadharNumber,
            length,
            breadth,
            area: (length * breadth).toFixed(2), // Automatically calculate area in sqft
            roofType,
            yearOfConstruction,
            drainageType,
            roadType,
            electricityConnectionType,
            houseType
        };

        try {
            const response = await fetch('/api/houses', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(houseDetails),
            });

            if (response.ok) {
                const data = await response.json();
                console.log(data.message); // Display success message
                // Reset form fields after submission
                setOwnerName('');
                setAadharNumber('');
                setLength('');
                setBreadth('');
                setRoofType('');
                setYearOfConstruction('');
                setDrainageType('');
                setRoadType('');
                setElectricityConnectionType('');
                setHouseType('');
            } else {
                throw new Error('Failed to submit details');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>House Details Form</h2>
            <label>
                Owner Name:
                <input
                    type="text"
                    value={ownerName}
                    onChange={(e) => setOwnerName(e.target.value)}
                    required
                />
            </label>
            <label>
                Aadhar Number:
                <input
                    type="text"
                    value={aadharNumber}
                    onChange={(e) => setAadharNumber(e.target.value)}
                    required
                />
            </label>
            <label>
                Length (ft):
                <input
                    type="number"
                    value={length}
                    onChange={(e) => setLength(e.target.value)}
                    required
                />
            </label>
            <label>
                Breadth (ft):
                <input
                    type="number"
                    value={breadth}
                    onChange={(e) => setBreadth(e.target.value)}
                    required
                />
            </label>
            <label>
                Roof Type:
                <select value={roofType} onChange={(e) => setRoofType(e.target.value)} required>
                    <option value="">Select</option>
                    <option value="Concrete">Concrete</option>
                    <option value="Tiled">Tiled</option>
                    <option value="Thatch">Thatch</option>
                    <option value="Metal">Metal</option>
                </select>
            </label>
            <label>
                Year of Construction:
                <input
                    type="number"
                    value={yearOfConstruction}
                    onChange={(e) => setYearOfConstruction(e.target.value)}
                    required
                />
            </label>
            <label>
                Drainage Type:
                <input
                    type="text"
                    value={drainageType}
                    onChange={(e) => setDrainageType(e.target.value)}
                    required
                />
            </label>
            <label>
                Road Type:
                <input
                    type="text"
                    value={roadType}
                    onChange={(e) => setRoadType(e.target.value)}
                    required
                />
            </label>
            <label>
                Electricity Connection Type:
                <input
                    type="text"
                    value={electricityConnectionType}
                    onChange={(e) => setElectricityConnectionType(e.target.value)}
                    required
                />
            </label>
            <label>
                House Type:
                <select value={houseType} onChange={(e) => setHouseType(e.target.value)} required>
                    <option value="">Select</option>
                    <option value="Living">Living</option>
                    <option value="Business">Business</option>
                </select>
            </label>
            <button type="submit">Submit</button>
        </form>
    );
};

export default HouseForm;
