# Pkill
exec {'killmenow':
command  => 'pkill',
onlyif => 'exec'
}

