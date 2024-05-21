import React, { useState, ChangeEvent, FormEvent } from 'react';
import {
    Container,
    Typography,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    TextField,
    Button,
    Alert,
    CircularProgress
} from '@mui/material';
import axios from 'axios';

const VB12 = () => {
    const [yValues, setYValues] = useState<string[]>(Array(9).fill(''));
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [graphUrl, setGraphUrl] = useState<string>('');

    const handleChange = (index: number, value: string) => {
        const newYValues = [...yValues];
        newYValues[index] = value;
        setYValues(newYValues);
    };

    const handleSubmit = async (event: FormEvent) => {
        event.preventDefault();
        setError(null);
        setLoading(true);
        setGraphUrl('');

        try {
            const response = await axios.post('https://api.ikeda042api.net/api/lab/vb12', { y: yValues.map(Number) });
            setGraphUrl(`https://api.ikeda042api.net/api/lab/lab_files/${response.data.graph_id}`);
        } catch (error: any) {
            setError(error.response ? error.response.data.error : 'An unexpected error occurred');
        } finally {
            setLoading(false);
        }
    };

    return (
        <Container>
            <Typography variant="h4" gutterBottom>VB12 Calibration Curve</Typography>
            <form onSubmit={handleSubmit}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell>X</TableCell>
                            <TableCell>Y</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {yValues.map((value, index) => (
                            <TableRow key={index}>
                                <TableCell>{[0, 0.1, 0.25, 0.5, 1, 2, 2.5, 4, 5][index]}</TableCell>
                                <TableCell>
                                    <TextField
                                        type="number"
                                        value={value}
                                        onChange={(e: ChangeEvent<HTMLInputElement>) => handleChange(index, e.target.value)}
                                        required
                                        fullWidth
                                    />
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
                <Button type="submit" variant="contained" color="primary" disabled={loading}>
                    Submit
                </Button>
                {loading && <CircularProgress />}
            </form>
            {error && <Alert severity="error">{error}</Alert>}
            {graphUrl && (
                <div>
                    <Typography variant="h6" gutterBottom>Generated Graph</Typography>
                    <img src={graphUrl} alt="Graph" style={{ maxWidth: '100%' }} />
                </div>
            )}
        </Container>
    );
};

export default VB12;
