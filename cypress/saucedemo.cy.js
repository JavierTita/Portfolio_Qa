describe('Saucedemo - Compra completa', function(){

    beforeEach(function(){
        cy.visit('https://www.saucedemo.com')
    })
    afterEach(function(){
        cy.screenshot()
    })

    it('Compra completa', function(){

        // LOGIN - usa el comando personalizado
        cy.loginCompleto()
        cy.screenshot('despues del login')

        // AGREGAR AL CARRITO
        cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()

        // VERIFICAR QUE SE AGREGÓ
        cy.get('[data-test="shopping-cart-badge"]').should('have.text', '1')

        // IR AL CARRITO
        cy.get('[data-test="shopping-cart-link"]').click()

        // CHECKOUT
        cy.get('[data-test="checkout"]').click()
        

        // COMPLETAR FORMULARIO - usa el comando personalizado
        cy.checkout()
        cy.screenshot('despues del checkout')

        // FINALIZAR COMPRA
        cy.get('[data-test="finish"]').click()

        // VERIFICAR COMPRA EXITOSA
        cy.get('[data-test="complete-header"]').should('have.text', 'Thank you for your order!')

        // VOLVER A PRODUCTOS
        cy.get('[data-test="back-to-products"]').click()

        

    })
})


