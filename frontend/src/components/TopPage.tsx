import { Typography } from '@mui/material';
import { Box } from '@mui/system';
import DrawerAppBar from './NavigationBar';
import VB12 from './VB12';

export default function TopPage() {
    return (
        <Box sx={{ bgcolor: "#f7f6f5", color: 'black', minHeight: '100vh' }}>
            <DrawerAppBar />
            <Typography variant="h1" align="center" sx={{ paddingTop: '20vh' }}>
                テスト
            </Typography>
            <VB12 />
        </Box>
    );
}