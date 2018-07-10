# -*- coding: utf-8 -*-

from odoo import models, fields, api

class rfid(models.Model):
    _name = 'barang'
    id_barang = fields.Char(string="ID", required=True)
    nama_barang = fields.Char(string="Nama Barang", required=True)


class rfidAPI(models.Model):
    _name = 'rfid.tag'
    hexcode = fields.Char(string="hex code")
    status = fields.Char(string="status tag")

class polybox(models.Model):
    _name = 'rfid.polybox'
    id_polybox = fields.Char(string="Hex Code Polybox", required=True)
    nama_polybox = fields.Char(string="Nama Polybox", required=True)
    status_polybox = fields.Selection([('terkirim', 'Polybag Terkirim'), ('tersedia', 'Polybog Tersedia')], default='tersedia', required=True)
    tgl_kirim = fields.Date(string="Tanggal Kirim Polybox")
    tgl_masuk = fields.Date(string="Tanggal Masuk Polybox")
    listProduct = fields.Integer(string="Jumlah Produk")
    deskripsi = fields.Char(string="Deskripsi Polybox")



#class rfid(models.Model):
	#_name = "rfid.barang"
	#3id_barang = fields.Char(string='ID' , required=True)
	#nama_barang = fields.Char(string='Nama Barang', required=True)
	

