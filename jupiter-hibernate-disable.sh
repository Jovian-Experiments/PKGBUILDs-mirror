#!/bin/sh
# Disable hibernate for Jupiter/Galileo at runtime

dropin_dir=/etc/systemd/sleep.conf.d/
dropin="$dropin_dir"/zz-holo-jupiter-nohibernate.conf

manufacturer=$(dmidecode -s system-manufacturer)
product=$(dmidecode -s system-product-name)

if [[ "$manufacturer" == "Valve" && ( "$product" == "Galileo" || "$product" == "Jupiter" ) ]]; then
	[ -f "$dropin" ] && exit 0

	mkdir -p "$dropin_dir"
	cat > "$dropin" <<EOF
[Sleep]
AllowHibernation=no
AllowSuspendThenHibernate=no
AllowHybridSleep=no
EOF
else
	rm -f "$dropin"
fi
