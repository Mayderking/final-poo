from django.urls import path
from .views import inicio, listar_productos, detalle_producto, agregar_producto, editar_producto, eliminar_producto, listar_clientes, agregar_cliente, editar_cliente, eliminar_cliente, listar_ventas, agregar_venta, reporte_ventas, listar_categorias, agregar_categoria, editar_categoria, eliminar_categoria, listar_proveedores, agregar_proveedor, editar_proveedor, eliminar_proveedor

urlpatterns = [
    #pagina de inicio
    path('', inicio, name='inicio'),

    #para productos
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('productos/añadir/', agregar_producto, name='agregar_producto'),
    path('producto/<int:pk>/editar/', editar_producto, name='editar_producto'),
    path('producto/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),

    #para clientes
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/añadir/', agregar_cliente, name='agregar_cliente'),
    path('clientes/<int:pk>/editar/', editar_cliente, name='editar_cliente'),
    path('clientes/<int:pk>/eliminar/', eliminar_cliente, name='eliminar_cliente'),

    #para ventas
    path('ventas/', listar_ventas, name='listar_ventas'),
    path('ventas/añadir/', agregar_venta, name='agregar_venta'),
    path('ventas/reporte/', reporte_ventas, name='reporte_ventas'),

    #para categorias
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', agregar_categoria, name='agregar_categoria'),
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),

    #para proveedor
    path('proveedores/', listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:pk>/', editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', eliminar_proveedor, name='eliminar_proveedor'),
]