import React, { useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import { Streamlit } from 'streamlit-component-lib';
import MicroSlats from './MicroSlats.jsx';

const App = () => {
  useEffect(() => {
    Streamlit.setComponentReady();
    Streamlit.setFrameHeight(0);

    // Tangkap pergerakan mouse dari layar utama Streamlit (window.parent)
    const onParentMouseMove = (e) => {
      window.dispatchEvent(new PointerEvent('pointermove', {
        clientX: e.clientX,
        clientY: e.clientY,
        bubbles: true
      }));
    };

    try {
      window.parent.addEventListener('pointermove', onParentMouseMove, { passive: true });
    } catch (err) {
      console.error(err);
    }

    return () => {
      try {
        window.parent.removeEventListener('pointermove', onParentMouseMove);
      } catch (err) {}
    };
  }, []);

  return (
    <div style={{
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100vw',
      height: '100vh',
      zIndex: -1,
      pointerEvents: 'none'
    }}>
<MicroSlats 
        preset="swell"
        color="#00F0FF"      // Electric Cyan
        glintColor="#A5F3FC"
        backgroundColor="#0A0E17"
        interactive={true}
        cursorStrength={1.5} // Dikecilkan dari 3.0 ke 1.5
        cursorSize={35}      // Dikecilkan dari 70 ke 35
      />
    </div>
  );
};

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);