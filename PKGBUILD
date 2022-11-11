# SPDX-License-Identifier: LGPL-2.1+
#
# Copyright (c) 2021 Valve.
# Maintainer: Guilherme G. Piccoli <gpiccoli@igalia.com>

pkgbase=kdump-steamos
pkgname=kdump-steamos
pkgver=0.9
_srctag=v0.9
pkgrel=2
pkgdesc="Kdump scripts to collect vmcore/dmesg in a small dracut-based initramfs"
makedepends=('git')
arch=('x86_64')
license=('GPL2')
install=kdump-steamos.install

source=("$pkgbase::git+https://gitlab.steamos.cloud/jupiter/kdump_steamos.git#tag=${_srctag}")
sha256sums=('SKIP')

package() {
	depends=('curl' 'dmidecode' 'dracut' 'jq' 'kexec-tools' 'makedumpfile' 'systemd' 'zip' 'zstd')

	cd $srcdir/$pkgname
	make install DESTDIR="${pkgdir}"
}
