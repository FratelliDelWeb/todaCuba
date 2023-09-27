const galleriaContenedor = document.querySelector('.galleria-contenedor');
const galleriaControlsContenedor = document.querySelector('.galleria-controls');
const galleriaControls = document.querySelector('previous', 'siguiente');
const galleriaItems = document.querySelectorAll('.galleria-item');

class Carrusel {
    constructor(contenedor, items, controls) {
        this.carruselContenedor = contenedor;
        this.carruselControls = controls;
        this.carruselArray = [...items];
    }

    updateGalleria() {
        this.carruselArray.forEach(el => {
            el.classList.remove('galleria-item-1');
            el.classList.remove('galleria-item-2');
            el.classList.remove('galleria-item-3');
            el.classList.remove('galleria-item-4');
            el.classList.remove('galleria-item-5');
        });

        this.carruselArray.slice(0, 5).forEach((el, i) => {
            el.classList.add(`galleria-item-${i+1}`);
        });
    }

    setCurrentState(direction) {
        if (direction.className == 'galleria-controls-previous') {
            this.carruselArray.unshift(this.carruselArray.pop());
        } else {
            this.carruselArray.push(this.carruselArray.shift());
        }
        this.updateGalleria();
    }
    setConstrols() {
        this.carruselControls.forEach(control => {
            galleriaControlsContenedor.apperdChild(document.createElement('button')).className = `galleria-controls-${control}`;
            document.querySelector('.galleria-controls${control}').innerText = control;
        });
    }

    useControls() {
        const triggers = [...galleriaControlsContenedor.childNodes];
        triggers.forEach(control => {
            control.addEventListener('click', e => {
                e.preventDefault();
                this.setCurrentState(control);
            });
        });
    }
}

const exampleCarrusel = new Carrusel(galleriaContenedor, galleriaItems, galleriaControls);
exampleCarrusel.setConstrols();
exampleCarrusel.useControls();










